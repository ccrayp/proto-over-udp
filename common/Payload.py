from uuid import *

SEPARATOR = "|"

class Payload:
    def __init__(self, id: UUID, command: str, args: list[str] = None):
        if not (id and command):
            self._isValid = False
            return

        self._id = id
        self._command = command
        self._args = args

        self._isValid = True

    def toString(self) -> str:
        if not self._isValid:
            return None

        if not self._args:
            return str(self._id)+ SEPARATOR + self._command

        return str(self._id) + SEPARATOR + self._command + SEPARATOR + self.argsToString()


    def prepare(self) -> bytes:
        if not self._isValid:
            return None
        
        return self.toString().encode("utf-8")


    def argsToString(self) -> str:
        if not self._isValid:
            return None

        if not self._args:
            return None
        
        argsString: str = ""
        for index, arg in enumerate(self._args):
            argsString += arg
            if index + 1 != len(self._args):
                argsString += SEPARATOR

        return argsString