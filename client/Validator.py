from common.Commands import ALLOWED_COMMANDS, ARGS_QTY_BY_COMMAND

class Validator:
    @staticmethod
    def validate(inputStr: str) -> tuple[bool, str, int]:
        result = Validator.checkStartSpaces(inputStr)
        if not result[0]:
            substring = result[1]
            return False, substring, 0

        result = Validator.checkEndSpaces(inputStr)
        if not result[0]:
            substring = result[1]
            errorPosition = result[2]
            return False, substring, errorPosition

        result = Validator.findForbiddenSymbols(inputStr)
        if not result[0]:
            invalidSymbol = result[1]
            errorPosition = result[2]
            substring = Validator.findForbiddenSubstring(inputStr, invalidSymbol, errorPosition)
            return False, substring, errorPosition
        
        tokens = inputStr.split(" ")
        result = Validator.checkAllowedCommands(tokens[0])
        
        if not result:
            return False, tokens[0], 0

        result = Validator.checkCommandArgs(tokens)
        if not result[0]:
            command = tokens[0]
            substring = inputStr.replace(command + " ", "")
            errorPosition = result[1]
            return False, substring, errorPosition

        return True, None, None


    @staticmethod
    def findForbiddenSymbols(inputStr: str) -> tuple[bool, str, int]:
        for i, char in enumerate(inputStr):
            # (не буква и не цифра) или (этот и следующий символы - пробелы)
            if not char.isalnum() and char not in [" ", "_"] or (char == " " and inputStr[i + 1] == " "):
                return False, char, i

        return True, None, None


    @staticmethod
    def findForbiddenSubstring(inputStr: str, forbiddenSymbol: str, position: int) -> str:
        if not inputStr or not forbiddenSymbol:
            return

        try:
            digilanValue = int(position)
            if digilanValue < 0:
                return
        except:
            return

        endOfForbiddenSymbols = inputStr.rfind(forbiddenSymbol) + 1
        forbiddenSymbolsQuantity = (endOfForbiddenSymbols - position)
        return forbiddenSymbol * forbiddenSymbolsQuantity


    @staticmethod
    def checkStartSpaces(inputStr: str) -> tuple[bool, str]:
        if not inputStr:
            return True, None

        if not inputStr.startswith(" "):
            return True, None

        endOfSpaces = 0
        for i, char in enumerate(inputStr):
            if char != " ":
                endOfSpaces = i
                break

        return False, " " * endOfSpaces


    @staticmethod
    def checkEndSpaces(inputStr: str) -> tuple[bool, str, int]:
        if not inputStr:
            return True, None, None

        if not inputStr.endswith(" "):
            return True, None, None

        reversedStartOfSpaces = 0
        for i, char in enumerate(inputStr[::-1]):
            if char != " ":
                reversedStartOfSpaces = i
                break

        startOfSpaces = len(inputStr) - reversedStartOfSpaces
        spacesQuantity = len(inputStr) - startOfSpaces
    
        return False, " " * spacesQuantity, startOfSpaces


    @staticmethod
    def checkAllowedCommands(command: str) -> bool:
        if not command:
            return False

        if command not in ALLOWED_COMMANDS:
            return False
    
        return True


    @staticmethod
    def checkCommandArgs(tokens: list[str]) -> tuple[bool, int]:
        if not tokens:
            return False, None
        
        argsQuantity = len(tokens) - 1
        command = tokens[0]
        errorPosition = len(command) + 1

        if argsQuantity not in ARGS_QTY_BY_COMMAND[command]:
            return False, errorPosition

        return True, None