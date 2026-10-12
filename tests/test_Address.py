import pytest
from common.Address import Address

IP = "192.168.0.102"
PORT = 80
ADDRESS_DATA = (IP, PORT)

constructorParams = [
    (ADDRESS_DATA, True),
    ((None, None), False),
    (("1270.0.0.1", None), False),
    ((IP, 90000), False)
]

toStingParams = [
    (ADDRESS_DATA, f"{IP}:{PORT}"),
    (None, None),
    ((None, None), None)
]

getAddressParams = [
    (ADDRESS_DATA, ADDRESS_DATA),
    (None, None),
    ((None, None), None)
]

class TestAddress:
    @pytest.mark.parametrize("addressData, expected_output", constructorParams)
    def test_constructor(self, addressData, expected_output):
        address = Address(addressData)

        assert address._isValid == expected_output


    @pytest.mark.parametrize("addressData, expected_output", toStingParams)
    def test_to_string(self, addressData, expected_output):
        address = Address(addressData)
        result = address.toString()

        assert result == expected_output


    @pytest.mark.parametrize("addressData, expected_output", getAddressParams)
    def test_get_address(self, addressData, expected_output):
        address = Address(addressData)
        result = address.getAddress()

        assert result == expected_output