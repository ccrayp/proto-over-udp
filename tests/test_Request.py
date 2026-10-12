import pytest
from common.Payload import Payload
from common.Address import Address
from common.Request import Request
from common.Response import Response

ADDRESS_DATA = ("127.0.0.1", 5011)

constructorParams = [
    (Payload(123, "LIST"), Address(ADDRESS_DATA), True),
    (Payload(123, "LIST"), Address(None), False),
    ("payload", None, False),
    (None, None, False)
]

getIdParams = [
    (Payload(123, "LIST"), Address(ADDRESS_DATA), 123),
    (Payload(123, "LIST"), Address(None), None),
    ("payload", None, None),
    (None, None, None)
]

class TestRequestResponse:
    @pytest.mark.parametrize("payload, address, expected_output", constructorParams)
    def test_request_constructor(self, payload: Payload, address: Address, expected_output):
        request = Request(payload, address)
        assert request._isValid == expected_output


    @pytest.mark.parametrize("payload, address, expected_output", constructorParams)
    def test_constructor(self, payload: Payload, address: Address, expected_output):
            response = Response(payload, address)
            assert response._isValid == expected_output


    @pytest.mark.parametrize("payload, address, expected_output", getIdParams)
    def test_get_id(self, payload: Payload, address: Address, expected_output):
        request = Request(payload, address)
        assert request.getId() == expected_output