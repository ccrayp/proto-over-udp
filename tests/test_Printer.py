import pytest
from common.PayloadFactory import PayloadFactory
from client.Printer import *

HELP_OUTPUT = "HELP - show this manual\nEXIT - close client application\n\nCOMMAND <args...>\n<?arg?> - optional argument\n<arg|arg> - two types of arguments\n\nADD <code> <name> <?quantity?>\nGET <code|name>\nSET_QTY <code> <quantity>\nDELETE <code>\nLIST\n"
ENTERANCE_OUTPUT = "> "

printerMethodsWithoutParams = [
     (Printer.showHelp, HELP_OUTPUT),
     (Printer.inputEnterance, ENTERANCE_OUTPUT),
     (Printer.newLine, "\n")
]

timeoutParams = [
    (0, 0, ""),
    (-1, -1, ""),
    (0, 1, ""),
    (1, 1, f"{YELLOW}Timeout{RESET}\nRetry 1/1\n"),
]

reportParams = [
    (0.0, 2, PayloadFactory.newOfArgs("OK", args=["C1 name 0"]), 3, f"Response:\n{GREEN}C1 name 0{RESET}\nRTT: 0.0000 ms\nRetries: 2\n"),
    (0.0, 2, None, 3, "")
]

invalidInputParams = [
    ("ADD Ice||| Мороженое", "|||", 7, f"Invalid input: ADD Ice||| Мороженое\n                      {RED}~~~{RESET}\n"),
    (None, None, -1, "")
]

underlineParams = [
    (3, 0, f"{RED}~~~{RESET}"),
    (0, 0, None),
    (-1, -1, None)
]

requestIdParams = [
    (PayloadFactory.newOfArgs("ADD", [""], id="123"), "Request #123\n"),
    (None, "")
]

payloadParams = [
    (PayloadFactory.newOfArgs("OK", ["123 Мороженое 0"], id="123"), f"Response:\n{GREEN}123 Мороженое 0{RESET}\n"),
    (PayloadFactory.newOfArgs("ERROR", ["Product with such identificator was not found"], id="123"), f"Response:\n{RED}Product with such identificator was not found{RESET}\n"),
    (None, "")
]


class TestPrinter:
    @pytest.mark.parametrize("printer_method, expected_output", printerMethodsWithoutParams)
    def test_printer_outputs_without_params(self, capsys: pytest.CaptureFixture, printer_method, expected_output):
        printer_method()
        captured = capsys.readouterr()
        assert captured.out == expected_output


    @pytest.mark.parametrize("tries, maxTries, expected_output", timeoutParams)
    def test_timeout(self, capsys: pytest.CaptureFixture, tries, maxTries, expected_output):
        Printer.timeout(tries, maxTries)
        captured = capsys.readouterr()
        assert captured.out == expected_output


    @pytest.mark.parametrize("time, tries, payload, maxTries, expected_output", reportParams)
    def test_report(self, capsys: pytest.CaptureFixture, time, tries, payload, maxTries, expected_output):
        Printer.report(time, tries, payload, maxTries)
        captured = capsys.readouterr()
        assert captured.out == expected_output


    @pytest.mark.parametrize("inputStr, invalidToken, errorPosition, expected_output", invalidInputParams)
    def test_invalid_input(self, capsys: pytest.CaptureFixture, inputStr, invalidToken, errorPosition, expected_output):
        Printer.invalidInput(inputStr, invalidToken, errorPosition)
        captured = capsys.readouterr()
        assert captured.out == expected_output


    @pytest.mark.parametrize("invalidTokenLength, errorPosition, expected_output", underlineParams)
    def test_underline(self, invalidTokenLength, errorPosition, expected_output):
        underline = Printer.underline(invalidTokenLength, errorPosition)
        assert underline == expected_output


    @pytest.mark.parametrize("payload, expected_output", requestIdParams)
    def test_request_id(self, capsys: pytest.CaptureFixture, payload, expected_output):
        Printer.printRequestId(payload)
        captured = capsys.readouterr()
        assert captured.out == expected_output


    @pytest.mark.parametrize("payload, expected_output", payloadParams)
    def test_payload(self, capsys: pytest.CaptureFixture, payload, expected_output):
        Printer.printPayload(payload)
        captured = capsys.readouterr()
        assert captured.out == expected_output