from server.Cache import Cache
from server.Logger import Logger
from server.Warehouse import Warehouse
from server.Processor import Processor
from server.SocketServer import SocketServer

from common.PayloadFactory import PayloadFactory
from common.Response import Response
from common.Commands import *

cache = Cache()
logger = Logger()
warehouse = Warehouse()
processor = Processor(warehouse)
socket = SocketServer("127.0.0.1", 5011)

while True:
    try:
        request = socket.recieve()
        logger.logRequest(request)

        responseData, responseStatus = cache.getDataByRequest(request)
        if responseData:
            logger.logUsingCache(request)
        else:
            responseData, responseStatus = processor.execute(request._payload)
            cache.initRecord(request)
            cache.setDataByRequest(request, responseData, responseStatus)

        responsePayload = PayloadFactory.newOfArgs(command=responseStatus, args=responseData, id=request.getId())
        response = Response(responsePayload, request._address)

        if socket.send(response):
            logger.logResponse(response)
        else:
            logger.logSendLoss()

        print()
    except KeyboardInterrupt:
        break
        