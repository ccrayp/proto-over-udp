import uuid

import pytest
from common.PayloadFactory import PayloadFactory
from common.Payload import Payload

newOfArgsParms = [
    ("ADD", ["Ice", "Мороженое", "10"], 123, Payload(123, "ADD", ["Ice", "Мороженое", "10"])),
    ("GET", None, None, Payload(123, "GET")),
    (None, None, None, Payload(None , None))
]

rawDataParams = [
    ("123 ADD Ice Мороженое 10", False, Payload(123, "ADD", ["Ice", "Мороженое", "10"])),
    ("123 LIST", False, Payload(123, "LIST")),
    ("123|ADD|Ice|Мороженое|10".encode("utf-8"), True, Payload(123, "ADD", ["Ice", "Мороженое", "10"])),
    (None, False, None)
]

class TestPayloadFactory:
    @pytest.mark.parametrize("command, args, id, expected_output", newOfArgsParms)
    def test_new_of_arg(self, command, args, id, expected_output: Payload):
        payload = PayloadFactory.newOfArgs(command, args, id)

        if not payload:
            return

        assert payload._isValid == expected_output._isValid
        assert payload._command == expected_output._command
        assert payload._args == expected_output._args
        assert payload._isValid == expected_output._isValid
        assert payload._id


    @pytest.mark.parametrize("rawData, toDecode, expected_output", rawDataParams)
    def test_of_raw_data(self, rawData, toDecode, expected_output):
        payload = PayloadFactory.newOfRawData(rawData, toDecode=toDecode)
        
        if not payload:
            return

        assert payload._isValid == expected_output._isValid
        assert payload._command == expected_output._command
        assert payload._args == expected_output._args
        assert payload._isValid == expected_output._isValid
        assert payload._id