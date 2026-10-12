import pytest
from common.Product import Product

constructorParams = [
    ("code", "name", None, True),
    (None, None, -1, False),
    (None, None, None, False)
]

quantityParams = [
    (Product("code", "name"), 12, True),
    (Product(None, None), 12, False),
    (Product("code", "name", 100), -1, False)
]

toStringParams = [
    (Product("code", "name"), "code name 0"),
    (Product("code", "name", 100), "code name 100"),
    (Product(None, None), None),
]

class TestProduct:
    @pytest.mark.parametrize("code, name, quantity, expected_output", constructorParams)
    def test_constructor(self, code, name, quantity, expected_output):
        product = Product(code, name, quantity)

        assert product._isValid == expected_output


    @pytest.mark.parametrize("product, quantity, expected_output", quantityParams)
    def test_set_quantity(self, product: Product, quantity, expected_output):
        product.setQuantity(quantity)

        assert (product._quantity == quantity) == expected_output


    @pytest.mark.parametrize("product, expected_output", toStringParams)
    def test_to_string(self, product: Product, expected_output):
        assert expected_output == product.toString()
