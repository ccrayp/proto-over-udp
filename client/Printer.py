from common.Payload import Payload, SEPARATOR
from common.Commands import ERROR_STATUS

RED = "\033[31m"
GREEN = "\033[32m"
YELLOW = "\033[33m"
RESET = "\033[0m"

class Printer:
    @staticmethod
    def showHelp():
        print("HELP - show this manual")
        print("EXIT - close client application")
        print()
        print("COMMAND <args...>")
        print("<?arg?> - optional argument")
        print("<arg|arg> - two types of arguments")
        print()
        print("ADD <code> <name> <?quantity?>")
        print("GET <code|name>")
        print("SET_QTY <code> <quantity>")
        print("DELETE <code>")
        print("LIST")


    @staticmethod
    def inputEnterance():
        print("> ", end="")


    @staticmethod
    def newLine():
        print()


    @staticmethod
    def timeout(tries: int, maxTries: int):
        if maxTries <= 0 or tries <= 0 or tries > maxTries:
            return
        print(YELLOW + "Timeout" + RESET)
        print(f"Retry {tries}/{maxTries}")


    @staticmethod
    def report(time: float, tries: int, payload: Payload, maxTries: int):
        if time < 0.0 or maxTries < 0 or tries < 0 or tries > maxTries or not payload:
            return
        Printer.printPayload(payload)
        print(f"RTT: {time:.4f} ms")
        print(f"Retries: {tries}")


    @staticmethod
    def invalidInput(inputStr: str, invalidToken: str, errorPosition: int):
        if not inputStr or not invalidToken or errorPosition < 0:
            return
        prefixStr = f"Invalid input: "
        print(f"{prefixStr}{inputStr}")
        print(Printer.underline(len(invalidToken), len(prefixStr) + errorPosition))


    @staticmethod
    def underline(invalidTokenLength: int, errorPosition: int) -> str:
        if invalidTokenLength <= 0 or errorPosition < 0:
            return
        underlineStr: str = " " * errorPosition
        underlineStr +=  RED + "~" * invalidTokenLength + RESET
        return underlineStr


    @staticmethod
    def printRequestId(payload: Payload):
        if not payload:
            return
        print(f"Request #{payload._id}")


    @staticmethod
    def printPayload(payload: Payload):
        if not payload:
            return
        print("Response:")
        data = payload.toString()
        products = data.split(SEPARATOR)[2::]
        if payload._command == ERROR_STATUS:
            print(RED + "\n".join(products) + RESET)
            return

        print(GREEN +"\n".join(products) + RESET)
