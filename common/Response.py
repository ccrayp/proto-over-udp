from common import Payload, Address
from common.Payload import Payload
from common.Address import Address

class Response:
    def __init__(self, payload: Payload, address: Address):
        if not address or not isinstance(address, Address) or not address._isValid:
            self._isValid = False
            return

        if not payload or not isinstance(payload, Payload) or not payload._isValid:
            self._isValid = False
            return
        
        self._payload = payload
        self._address = address
        self._isValid = True