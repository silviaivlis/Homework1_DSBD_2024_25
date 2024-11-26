import yfinance as yf
from circuitBreaker import CircuitBreaker
import time
from datetime import datetime, timedelta
from database import Session, FinancialData, Users

def getPrice(ticker):
    values = yf.Ticker(ticker).history(period="1d") 
    if values.empty:
        raise ValueError(f"Nessun valore trovato per {ticker}")
    return values


def dataCollector(session, circuitBreaker):
    error_occurred = False
    try:
        users = session.query(Users).all()
        if not users:
            print("Nessun utente trovato nel database.")
        for user in users:
            try:
                tickerPrices = circuitBreaker.call(getPrice, user.ticker)
                
                if 'Close' not in tickerPrices.columns or tickerPrices['Close'].isnull().all():
                    raise ValueError(f"Nessun valore 'Close' valido per il ticker {user.ticker}")
                price = float(tickerPrices['Close'].iloc[0])

                session.add(FinancialData(
                    ticker = user.ticker,
                    value = price
                ))
                session.commit()

            except Exception as e:
                error_occurred = True
                print(f"Errore durante l'elaborazione del ticker. {e}")

    except Exception as e:
        error_occurred = True
        print(f"Errore generale nella funzione dataCollector: {e}")
    finally:
        if not error_occurred:
            print("Ciclo di raccolta dati completato, attendo 3 minuti per recuperare il nuovo valore")
        else:
            print("Ciclo di raccolta dati completato con errori, attendo 3 minuti prima di riprovare")


def cleanData(session):
    ticks = session.query(FinancialData.ticker).distinct().all()
    tickers = [t[0] for t in ticks]

    for ticker in tickers:
        totRecords = session.query(FinancialData).filter_by(ticker=ticker).count()

        if totRecords > 20:
            recordsToDelete = totRecords - 20
            oldRecords = session.query(FinancialData.id).filter_by(ticker=ticker).order_by(FinancialData.timestamp.asc()).limit(recordsToDelete).all()
            oldRecordID = [record.id for record in oldRecords]
            session.query(FinancialData).filter(FinancialData.id.in_(oldRecordID)).delete(synchronize_session=False)
            session.commit()
            print(f"Eliminati {recordsToDelete} vecchi record per il ticker {ticker}")
        else:
            print(f"Nessun record da eliminare per il ticker {ticker}")


def main():
    circuitBreaker = CircuitBreaker(failure_threshold=3, recovery_timeout=60)
    lastCleanTime = datetime.now() 
    cleanInterval = timedelta(hours=12)

    while True:
        startTime = datetime.now()
        print(f"Inizio raccolta dati alle {startTime.strftime('%H:%M:%S')}")
        with Session() as session:
            dataCollector(session, circuitBreaker)
        
        currentTime = datetime.now()
        lastClean = currentTime - lastCleanTime
        if lastClean >= cleanInterval:
            print(f"Inizio pulizia dei dati alle {currentTime.strftime('%H:%M:%S')}")
            with Session() as session:
                cleanData(session)
            print("Pulizia completata.")
            lastCleanTime = currentTime
        else:
            timeRemaining = cleanInterval - lastClean
            print(f"Prossima pulizia tra {str(timeRemaining).split('.')[0]}")

        time.sleep(60)

if __name__ == "__main__":
    main()
