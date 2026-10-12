import datetime
from common.Request import Request
from common.Response import Response

class Logger:
    @staticmethod
    def logRequest(request: Request):
        if not request:
            print(f"{Logger.timestampPrefix()} Empty request")
            return
        
        print(f"{Logger.timestampPrefix()} {request._address.toString()} -> {request._payload.toString()}")


    @staticmethod
    def logUsingCache(request: Request):
        if not request:
            print(f"{Logger.timestampPrefix()} Empty request")
            return
        
        print(f"{Logger.timestampPrefix()} Using cached data for {request.getId()}")
        

    @staticmethod
    def logResponse(response: Response):
        if not response:
            print(f"{Logger.timestampPrefix()} Empty response")
            return
        
        print(f"{Logger.timestampPrefix()} Response: {response._payload.toString()}")


    @staticmethod
    def logSendLoss():
        print(f"{Logger.timestampPrefix()} Simulated response loss")


    @staticmethod
    def timestampPrefix():
        return f"[{datetime.datetime.now().time().replace(microsecond=0)}]"