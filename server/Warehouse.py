from common.Product import Product
from common.Payload import SEPARATOR

class Warehouse:
    def __init__(self):
        self._storage: list[Product] = []


    def addProduct(self, product: Product):
        self._storage.append(product)


    def removeProduct(self, id) -> bool:
        product, _ = self.findProductById(id)
        if product is None:
            return False
        
        self._storage.remove(product)
        return True


    def setProductQuantity(self, id, quantity: int) -> bool:
        _, index = self.findProductById(id)

        if index == -1:
            return False

        self._storage[index].setQuantity(quantity)
        
        return True


    def listProducts(self) -> str:
        listString = []
        for product in self._storage:
            listString.append(product.toString())

        return SEPARATOR.join(listString)


    def findProductById(self, id) -> tuple[Product, int]:
        product: Product = None
        index: int = None
        for index, tempProduct in enumerate(self._storage):
            if tempProduct._code == id:
                return tempProduct, index

        return None, -1


    def findProductByName(self, name) -> tuple[Product, int]:
        product: Product = None
        index: int = None
        for index, tempProduct in enumerate(self._storage):
            if tempProduct._name == name:
                return tempProduct, index

        return None, -1