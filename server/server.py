from __future__ import print_function
from concurrent import futures
import re
from threading import Lock
import logging
import yfinance as yf
import requests

import grpc
from database import Session, Engine, BaseClass
from database import FinancialData, Users
from proto import op_pb2, op_pb2_grpc

BaseClass.metadata.create_all(bind=Engine)

idRequestCache = {}
cache_lock = Lock()

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


class UserService(op_pb2_grpc.User_serviceServicer):
    #------------------------------------------------------------FUNZIONE_1 
    def RegisterUser(self,request,context):
        email = request.email
        ticker = request.ticker
        requestId = request.requestId

        with cache_lock:
            if requestId in idRequestCache:
                logging.warning(f"id {requestId} duplicato")
                return idRequestCache[requestId]
            
        session = Session()
        if verifyEmail(email) and verifyTicker(ticker):
            user = session.query(Users).filter_by(email=email).first()
            if user:
                response = op_pb2.RegUserResponse(message="Errore registrazione: utente già esistente con questa email!")
            else:
                newUser = Users(email=email,ticker=ticker)
                session.add(newUser)
                session.commit()
                response = op_pb2.RegUserResponse(message="Utente registrato correttamente!")

            with cache_lock:
                idRequestCache[requestId] = response

            return response
        
        print("Formato email non valido")

        
    #------------------------------------------------------------FUNZIONE_2 
    def UpdateUser(self,request,context):
        email = request.email
        ticker = request.ticker
        requestId = request.requestId

        with cache_lock:
            if requestId in idRequestCache:
                print(f"id {requestId} duplicato")
                return idRequestCache[requestId]

        session = Session()
        if verifyEmail(email) and verifyTicker(ticker):
            user = session.query(Users).filter_by(email=email).first()
            if user:
                if user.ticker == ticker:
                    response = op_pb2.UpdateUserResponse(message="L'utente possiede già questo ticker!")
                else:
                    user.ticker = ticker
                    session.commit()
                    response = op_pb2.UpdateUserResponse(message="Utente aggiornato correttamente!")
            else:
                response = op_pb2.UpdateUserResponse(message="Utente non esistente!")
        
            with cache_lock:
                idRequestCache[requestId] = response

            return response
        
        print("Formato email non valido")
        
    #------------------------------------------------------------FUNZIONE_3 
    def DeleteUser(self,request,context):
        email = request.email
        requestId = request.requestId

        with cache_lock:
            if requestId in idRequestCache:
                print(f"id {requestId} duplicato")
                return idRequestCache[requestId]
        
        session = Session()
        if verifyEmail(email):
            user = session.query(Users).filter_by(email=email).first()

            if user:
                session.delete(user)
                session.commit()
                response = op_pb2.UpdateUserResponse(message="Utente eliminato correttamente!")
            else:
                response = op_pb2.UpdateUserResponse(message="Utente non esistente!")
        
            with cache_lock:
                idRequestCache[requestId] = response

            return response
        
        print("Formato email non valido")

    #------------------------------------------------------------FUNZIONE_4 
    def GetLatestValue(self,request,context):
        email = request.email

        session = Session()
        if verifyEmail(email):
            user = session.query(Users).filter_by(email=email).first()
            if user:
                ticker = user.ticker
                if ticker:
                    latestData = session.query(FinancialData).filter_by(ticker=ticker).order_by(FinancialData.timestamp.desc()).first()

                    if latestData:
                        return op_pb2.GetLatestValueResponse(
                            email = email,
                            ticker = ticker,
                            value = latestData.value,
                            timestamp = latestData.timestamp.isoformat()
                        )
                    else:
                        return op_pb2.GetLatestValueResponse(
                            email = email,
                            ticker = ticker,
                            value = None,
                            timestamp = None
                        )
                #caso ticker non presente
                return op_pb2.GetLatestValueResponse(
                    email = email,
                    ticker = None,
                    value = None,
                    timestamp = None
                )
            #caso utente non esistente
            else:
                return op_pb2.GetLatestValueResponse(
                    email = None,
                    ticker = None,
                    value = None,
                    timestamp = None
            )
        else:
            print("Formato email non valido")

    #------------------------------------------------------------FUNZIONE_5 
    def CalcAvarageValue(self,request,context):
        email = request.email
        numValue = request.count

        session = Session()
        if verifyEmail(email):
            user = session.query(Users).filter_by(email=email).first()
            if user:
                ticker = (session.query(Users).filter_by(email=email).first()).ticker
                if ticker:
                    values = session.query(FinancialData).filter_by(ticker=ticker).order_by(FinancialData.timestamp.desc()).limit(numValue).all()

                    if len(values) > 0:
                        avarageValue = sum([value.value for value in values])/len(values)
                        return op_pb2.CalcAvarageValueResponse(
                            email = email,
                            ticker = ticker,
                            averageValue = avarageValue
                        )
                    else:
                        return op_pb2.CalcAvarageValueResponse(
                                email = email,
                                ticker = ticker,
                                averageValue = None
                        )
                #caso ticker non presente
                return op_pb2.CalcAvarageValueResponse(
                    email = email,
                    ticker = None,
                    averageValue = None
                )
            else:
                #caso utente non esistente
                return op_pb2.CalcAvarageValueResponse(
                    email = None,
                    ticker = None,
                    averageValue = None
                )
        else:
            print("Formato email non valido")


def serve():
    port='50051'
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    op_pb2_grpc.add_User_serviceServicer_to_server(UserService(), server)
    server.add_insecure_port("[::]:" + port)
    server.start()
    print("Server started, in ascolto sulla porta: " + port)
    server.wait_for_termination()


if __name__ == "__main__":
    serve()