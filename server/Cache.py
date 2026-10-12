from uuid import UUID
from common.Request import Request
from common.Commands import OK_STATUS, ERROR_STATUS

class Cache:
    def __init__(self):
        self._storage = {}


    def initRecord(self, request: Request):
        if not request:
            return
        
        self._storage[request.getId()] = None


    def listRecords(self) -> dict[UUID, any]:
        return self._storage


    def setDataByRequest(self, request: Request, data: any, status: any):
        if not request or not isinstance(request, Request):
            return

        if not data:
            return

        if status not in [OK_STATUS, ERROR_STATUS]:
            return
        
        self._storage[request.getId()] = (data, status)


    def getDataByRequest(self, request: Request) -> tuple[any, any]:
        if not request or not isinstance(request, Request):
            return None, None

        try:
            return self._storage[request.getId()]
        except:
            return None, None


    def removeByRequest(self, request: Request):
        if not request or isinstance(request, Request):
            return
        
        self._storage.pop(request.getId())
