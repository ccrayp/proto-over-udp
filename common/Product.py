class Product:
    def __init__(self, code: str, name: str, quantity: int = None):
        if not code or not name:
            self._code = None
            self._name = None
            self._quantity = 0
            self._isValid = False
            return

        self._code = code
        self._name = name
        self._quantity = 0
        if quantity and quantity > 0:
            self._quantity = quantity

        self._isValid = True


    def setQuantity(self, quantity: int):
        if not self._isValid:
            return

        if quantity < 0:
            return
        
        self._quantity = quantity


    def toString(self) -> str:
        if not self._isValid:
            return None
        
        return f"{self._code} {self._name} {self._quantity}"
