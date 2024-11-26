import re
import logging
import yfinance as yf
import grpc
import random
from proto import op_pb2, op_pb2_grpc
import requests

logging.getLogger("yfinance").setLevel(logging.CRITICAL)


def checkConnection():
    try:
        requests.get("https://finance.yahoo.com", timeout=5)
        return True
    except requests.ConnectionError:
        return False
    

def verifyTicker(ticker):
    if not checkConnection():
        print("Errore di connesione: controlla la tua rete.")
    else:
        data = yf.download(ticker, period="1d", progress=False)
        if data.empty:
            print(f"Verifica del ticker '{ticker}' errata: nessun dato trovato.")
            return False
        else:
            print(f"Verifica del ticker '{ticker}' andata a buon fine. Dato trovato")
            return True


def verifyEmail(email):
    pattern = r'^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$'
    return re.match(pattern, email) is not None


def generateIdRequest(operation, email, ticker=None):
    randNum = random.randint(0, 9999)
    ranNumformatted = f"{randNum:04}"
    uniqueString = "{}{}{}{}".format(operation, email, ticker if ticker else '', ranNumformatted)
    return uniqueString


def run() : 
    print("Eseguo un collegamento con il server!")
    with grpc.insecure_channel('localhost:50051') as channel:
        stub = op_pb2_grpc.User_serviceStub(channel)

        while True:
            print("\n|-------------------------------------------------------|")
            print("\nSeleziona un'operazione:")
            print("1. Registrazione utente")
            print("2. Aggiornamento utente")
            print("3. Cancellazione utente")
            print("4. Recupero dell'ultimo valore disponibile dell'azione")
            print("5. Calcolare la media degli ultimi X valori dell'azione")
            print("6. Esci")
            print("\n|-------------------------------------------------------|")
            print("\n")
            scelta = input("Inserisci il numero dell'operazione desiderata: ")

            #------------------------------------------------------------FUNZIONE_1
            if scelta == '1':
                while True:
                    email = input("Inserisci l'email relativa all'utente che vuoi registrare: ")
                    email_valid = verifyEmail(email)
                    if email_valid:
                        break
                    print("Formato email errato!")
                while True:
                    ticker = input("Inserisci il ticker: ")
                    ticker_valid = verifyTicker(ticker)
                    if ticker_valid:
                        break
                    
                if email_valid and ticker_valid:
                    operation = 'RegisterUser'
                    id_Request = generateIdRequest(operation, email)

                    response = stub.RegisterUser(op_pb2.RegUserRequest(
                        email=email, 
                        ticker=ticker,
                        requestId=id_Request
                    ))

                    # implementazione retry
                    # if not response.message.strip():
                    #     print("Retry...")
                    #     response = stub.RegisterUser(op_pb2.RegUserRequest(
                    #     email=email, 
                    #     ticker=ticker,
                    #     requestId=id_Request
                    # ))

                    print(response.message)


            #------------------------------------------------------------FUNZIONE_2
            elif scelta == '2':
                while True:
                    email = input("Inserisci l'email relativa all'utente di cui si vuole aggiornare il ticker: ")
                    email_valid = verifyEmail(email)
                    if email_valid:
                        break
                    print("Formato email errato!")
                while True:
                    ticker = input("Inserisci il nuovo ticker: ")
                    ticker_valid = verifyTicker(ticker)
                    if ticker_valid:
                        break
                    
                if email_valid and ticker_valid:
                    operation = 'UpdateUser'
                    id_Request = generateIdRequest(operation, email, ticker)

                    response = stub.UpdateUser(op_pb2.UpdateUserRequest(
                        email=email, 
                        ticker=ticker,
                        requestId = id_Request
                    ))
                    print(response.message)

            #------------------------------------------------------------FUNZIONE_3
            elif scelta == '3':
                while True:
                    email = input("Inserisci l'email relavita all'utente che si vuole eliminare: ")
                    if verifyEmail(email):
                        break
                    print("Formato email errato!")

                operation = 'DeleteUser'
                id_Request = generateIdRequest(operation, email)

                response = stub.DeleteUser(op_pb2.DeleteUserRequest(
                    email=email,
                    requestId = id_Request
                ))
                print(response.message)

            #------------------------------------------------------------FUNZIONE_4
            elif scelta == '4':
                while True:
                    while True:
                        email = input("Inserisci l'email relavita all'utente da cui recuperare il valore: ")
                        if verifyEmail(email):
                            break
                        print("Formato email errato!")

                    response = stub.GetLatestValue(op_pb2.GetLatestValueRequest(email=email))
                    if not response.email:
                        print("Errore: Utente non esistente.")
                    elif not response.value and not response.timestamp:
                        print("Errore: Nessun dato finanziario trovato per il ticker.")
                    else:
                        print(f"Ultimo valore di {response.ticker}: {response.value} | (Timestamp: {response.timestamp})")
                        break

            #------------------------------------------------------------FUNZIONE_5
            elif scelta == '5':
                while True:
                    while True:
                        email = input("Inserisci l'email relavita all'utente: ")
                        email_valid = verifyEmail(email)
                        if email_valid:
                            break
                        print("Formato email errato!")
                    while True:
                        try: 
                            numValue = int(input("Inserisci il numero di valori per eseguire la media: "))
                            if numValue > 0:
                                break
                            else:
                                print("Non puoi inserire un valore negativo o zero!")
                        except ValueError:
                            print("Errore: devi inserire un numero intero valido!")

                    if email_valid and numValue > 0:
                        response = stub.CalcAvarageValue(op_pb2.CalcAvarageValueRequest(email=email, count=numValue))
                        if not response.email:
                            print("Errore: Utente non esistente.")
                        elif not response.averageValue:
                            print("Errore: Nessun dato disponibile per calcolare la media.")
                        else:
                            print(f"Il valore medio di {response.ticker} è {response.averageValue}")
                            break
                    
            #------------------------------------------------------------ALTRO
            elif scelta == '6':
                print("\nEsco!")
                break

            else:
                print("\nScelta non valida, riprova.")


if __name__ == "__main__" : 
    logging.basicConfig()
    run()