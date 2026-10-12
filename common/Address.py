import ipaddress

class Address:
    def __init__(self, address):
        try:
            self._ip = address[0]
            self._port = address[1]

            if not self._ip or not self._port:
                raise TypeError

            ipaddress.ip_address(self._ip)

            if self._port < 0 or self._port > 65536:
                raise TypeError

            self._isValid = True
        except (IndexError, TypeError, ValueError):
            self._ip = None
            self._port = None
            self._isValid = False


    def toString(self) -> str:
        if not self._isValid:
            return None
        
        return f"{self._ip}:{self._port}"


    def getAddress(self) -> tuple[str, int]:
        if not self._isValid:
            return None
        
        return (self._ip, self._port)