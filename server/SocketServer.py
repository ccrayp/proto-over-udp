import random
from socket import *
from common.Response import Response
from common.Request import Request
from common.PayloadFactory import PayloadFactory
from common.Address import Address

class SocketServer:
    def __init__(self, ip: str, port: int):
        self._socket = socket(AF_INET, SOCK_DGRAM)
        self._address = (ip, port)
        self._socket.bind((ip, port))

    def recieve(self) -> Request:
        rawPayload, address = self._socket.recvfrom(4096)
        return Request(PayloadFactory.newOfRawData(rawData=rawPayload, toDecode=True), Address(address))


    def send(self, response: Response) -> bool:
        if random.random() < 0.3:
          return False

        self._socket.sendto(response._payload.prepare(), response._address.getAddress())
        return True