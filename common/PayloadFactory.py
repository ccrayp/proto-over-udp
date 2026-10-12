from uuid import UUID, uuid4
from common.Payload import Payload, SEPARATOR

class PayloadFactory:
    @staticmethod
    def newOfArgs(command: str, args: list[str] | None = None, id: UUID | None = None) -> Payload:
        if not command:
            return None
        if not id:
            id = uuid4()

        return Payload(id, command, args)

    @staticmethod
    def newOfRawData(rawData, generateId: bool = False, toDecode: bool = False):
        if not rawData:
            return None

        separator = " "
        if generateId:
            rawData = str(uuid4()) + " " + rawData
        if toDecode:
            rawData = rawData.decode("utf-8")
            separator = SEPARATOR

        tokens = rawData.split(separator)
        id = tokens[0]
        command = tokens[1]
        try:
            args = tokens[2::]
            if not len(args):
                args = None

            return Payload(id, command, args)
        except:
            print("Invalid payload: ", rawData)