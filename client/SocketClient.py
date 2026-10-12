from socket import *
from common.PayloadFactory import PayloadFactory
from common.Payload import Payload

MAX_TRIES = 3

class SocketClient:
    def __init__(self, ip: str, port: int):
        self._socket = socket(AF_INET, SOCK_DGRAM)
        self._address = (ip, port)
        self._socket.settimeout(2.0)


    def transmit(self, payload: Payload):
        self._socket.sendto(payload.prepare(), self._address)


    def recieve(self) -> Payload:
        rawPayload: Payload = None
        try:
            rawPayload, _ = self._socket.recvfrom(4096)
        except TimeoutError:
            return None

        return PayloadFactory.newOfRawData(rawData=rawPayload, toDecode=True)