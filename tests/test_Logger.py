import datetime

import pytest
from server.Logger import Logger
from common.Request import Request
from common.Response import Response
from common.Address import Address
from common.PayloadFactory import PayloadFactory

requestParams = [
    (Request(PayloadFactory.newOfArgs("ADD", ["Code", "Name"], id="123"), Address(("127.0.0.1", 5011))), f"{Logger.timestampPrefix()} 127.0.0.1:5011 -> 123|ADD|Code|Name\n"),
    (None, f"{Logger.timestampPrefix()} Empty request\n")
]

cacheParams = [
    (Request(PayloadFactory.newOfArgs("ADD", ["Code", "Name"], id="123"), Address(("127.0.0.1", 5011))), f"{Logger.timestampPrefix()} Using cached data for 123\n"),
    (None, f"{Logger.timestampPrefix()} Empty request\n")
]

responseParams = [
    (Response(PayloadFactory.newOfArgs("OK", ["Code Name 0"], id="123"), Address(("127.0.0.1", 5011))), f"{Logger.timestampPrefix()} Response: 123|OK|Code Name 0\n"),
    (None, f"{Logger.timestampPrefix()} Empty response\n")
]

class TestLogegr:
    @pytest.mark.parametrize("requestObject, expected_output", requestParams)
    def test_result(self, capsys: pytest.CaptureFixture, requestObject, expected_output):
        Logger.logRequest(requestObject)
        captured = capsys.readouterr()
        assert captured.out == expected_output


    @pytest.mark.parametrize("requestObject, expected_output", cacheParams)
    def test_cache(self, capsys: pytest.CaptureFixture, requestObject, expected_output):
        Logger.logUsingCache(requestObject)
        captured = capsys.readouterr()
        assert captured.out == expected_output


    @pytest.mark.parametrize("responseObject, expected_output", responseParams)
    def test_response(self, capsys: pytest.CaptureFixture, responseObject, expected_output):
        Logger.logResponse(responseObject)
        captured = capsys.readouterr()
        assert captured.out == expected_output


    def test_loss(self, capsys: pytest.CaptureFixture):
        Logger.logSendLoss()
        captured = capsys.readouterr()
        assert captured.out == f"{Logger.timestampPrefix()} Simulated response loss\n"


    def test_prefix(self):
        prefix = Logger.timestampPrefix()
        expected_prefix = f"[{datetime.datetime.now().time().replace(microsecond=0)}]"
        assert prefix == expected_prefix