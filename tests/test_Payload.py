import pytest
from common.Payload import Payload, SEPARATOR

constructorParams = [
    (123, "GET", ["1"], True),
    (123, "", ["1"], False),
    (None, "GET", ["code"], False)
]

toStringParams = [
    (Payload(123, "GET", ["1"]), "123" + SEPARATOR + "GET" + SEPARATOR + "1"),
    (Payload(123, "LIST"), "123" + SEPARATOR + "LIST"),
    (Payload(-1, None), None)
]

prepareParams = [
    (Payload(123, "GET", ["1"]), "123|GET|1".encode("utf-8")),
    (Payload(123, "LIST"), "123|LIST".encode("utf-8")),
    (Payload(-1, None), None)
]

argsToStringParams = [
    (Payload(123, "ADD", ["Ice", "Мороженое", "10"]), "Ice|Мороженое|10"),
    (Payload(123, "ADD"), None),
    (Payload(-1, None), None)
]

class TestPayload:
    @pytest.mark.parametrize("id, command, args, expected_output", constructorParams)
    def test_constructor(self, id, command, args, expected_output):
        payload = Payload(id, command, args)

        assert payload._isValid == expected_output


    @pytest.mark.parametrize("payload, expected_output", toStringParams)
    def test_to_string(self, payload: Payload, expected_output):
        assert expected_output == payload.toString()


    @pytest.mark.parametrize("payload, expected_output", prepareParams)
    def test_prepare(self, payload: Payload, expected_output):
        assert payload.prepare() == expected_output


    @pytest.mark.parametrize("payload, expected_output", argsToStringParams)
    def test_args_to_string(self, payload: Payload, expected_output):
        assert payload.argsToString() == expected_output