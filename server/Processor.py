from common.Payload import Payload
from server.Warehouse import Warehouse
from common.Commands import *
from common.Product import Product

class Processor:
    def __init__(self, warehouse: Warehouse):
        self._warehouse = warehouse
        self._handlers = {
            ADD_COMMAND: self.addHandler,
            GET_COMMAND: self.getHandler,
            SET_QTY_COMMAND: self.setQuantityHandler,
            DELETE_COMMAND: self.deleteHandler,
            LIST_COMMAND: self.listHandler
        }

    def execute(self, payload: Payload) -> tuple[list[any], str]:
        command = payload._command
        if command not in ALLOWED_COMMANDS:
            return [f"Invalid command <{command}>"], ERROR_STATUS

        argsQuantity: int = 0
        try:
            argsQuantity = len(payload._args)
        except:
            pass

        if argsQuantity not in ARGS_QTY_BY_COMMAND[command]:
            return [f"Invalid args quantity <{argsQuantity}>"], ERROR_STATUS

        return self._handlers[command](payload._args)


    def addHandler(self, args: list[any]) -> tuple[list[str], str]:
        if not args[0] and not args[1]:
            return ["One or both of args are empty"], ERROR_STATUS

        if self._warehouse.findProductByName(args[1])[0] or self._warehouse.findProductById(args[0])[0]:
            return ["Product with same data already eixsts"], ERROR_STATUS

        quantity = None
        try:
            quantity = int(args[2])
        except IndexError:
            pass
        except (ValueError, TypeError):
            return [f"Invalid quantity"], ERROR_STATUS
        product = Product(args[0], args[1], quantity)
        self._warehouse.addProduct(product)

        return ["Product was successfully added"], OK_STATUS


    def getHandler(self, args: list[any]) -> tuple[list[str], str]:
        if not args[0]:
            return ["Identificator is empty"], ERROR_STATUS

        reaultSearchById = self._warehouse.findProductById(args[0])
        product = reaultSearchById[0]
        if product:
            return [product.toString()], OK_STATUS

        resultSearchByName = self._warehouse.findProductByName(args[0])
        product = resultSearchByName[0]
        if product:
            return [product.toString()], OK_STATUS

        return ["Product with such identificator was not found"], ERROR_STATUS


    def setQuantityHandler(self, args: list[any]) -> tuple[list[str], str]:
        try:
            if not args[0] or int(args[1]) < 0:
                return [f"Empty identificator or invalid quantity <{args[1]}>"], ERROR_STATUS
        except:
            return [f"Invalid quantity"], ERROR_STATUS

        if not self._warehouse.setProductQuantity(args[0], args[1]):
            return [f"Product with such identificator was not found"], ERROR_STATUS

        return [f"Quantity <{args[1]}> was successfully set for product <{args[0]}>"], OK_STATUS


    def deleteHandler(self, args: list[any]):
        if not args[0]:
            return ["Identificator is empty"], ERROR_STATUS

        if not self._warehouse.removeProduct(args[0]):
            return ["Product with such identificator was not found"], ERROR_STATUS

        return ["Product was successfullt deleted"], OK_STATUS


    def listHandler(self, _: list[any]):
        return [self._warehouse.listProducts()], OK_STATUS