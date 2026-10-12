import pytest
from client.Validator import Validator

validateParams = [
    ("add", (False, "add", 0)),
    (" ADD", (False, " ", 0)),
    ("LIST ", (False, " ", 4)),
    ("GET 1 2", (False, "1 2", 4)),
    ("ADD Ice ∑∑∑ 4", (False, "∑∑∑", 8)),
    ("", (False, "", 0)),
    ("DELETE", (False, "DELETE", 7)),
    ("UPDATE Ice New_Code", (False, "UPDATE", 0))
]

forbiddenSymbolParams = [
    ("GET !", (False, "!", 4)),
    ("GET  ", (False, " ", 3)),
    ("", (True, None, None)),
    ("ADD Ice Мороженое 10", (True, None, None))
]

forbiddenSubstringParams = [
    ("GET !!!", "!", 4, "!!!"),
    ("GET >>>", None, None, None),
    ("GET >>>", ">", None, None),
    (None, "?", None, None),
]

startSpacesParams = [
    ("GET 1", (True, None)),
    (" GET 1", (False, " ")),
    ("     GET 1", (False, "     ")),
    (None, (True, None))
]

endSpacesParams = [
    ("GET 1 ", (False, " ", 5)),
    ("DELETE 1     ", (False, "     ", 8)),
    (None, (True, None, None)),
    ("???", (True, None, None))
]

allowedCommandsParams = [
    ("ADD", True),
    ("add", False),
    (None, False)
]

commandArgsParams = [
    (["ADD", "Ice", "Мороженое", "10"], (True, None)),
    (["LIST"], (True, None)),
    (["DELETE", "Code", "Name"], (False, 7)),
    (None, (False, None))
]

class TestValidator:
    @pytest.mark.parametrize("inputStr, expected_output", validateParams)
    def test_validate(self, inputStr, expected_output):
        checkResult = Validator.validate(inputStr)
        assert checkResult == expected_output


    @pytest.mark.parametrize("inputStr, expected_output", forbiddenSymbolParams)
    def test_find_forbidden(self, inputStr, expected_output):
        checkResult = Validator.findForbiddenSymbols(inputStr)
        assert checkResult == expected_output


    @pytest.mark.parametrize("inputStr, forbiddenSymbol, position, expected_output", forbiddenSubstringParams)
    def test_find_forbidden_substring(self, inputStr, forbiddenSymbol, position, expected_output):
        checkResult = Validator.findForbiddenSubstring(inputStr, forbiddenSymbol, position)
        assert checkResult == expected_output


    @pytest.mark.parametrize("inputStr, expected_output", startSpacesParams)
    def test_check_start_spaces(self, inputStr, expected_output):
        checkResult = Validator.checkStartSpaces(inputStr)
        assert checkResult == expected_output


    @pytest.mark.parametrize("inputStr, expected_output", endSpacesParams)
    def test_check_end_spaces(self, inputStr, expected_output):
        checkResult = Validator.checkEndSpaces(inputStr)
        assert checkResult == expected_output


    @pytest.mark.parametrize("command, expected_output", allowedCommandsParams)
    def test_check_allowed_commands(self, command, expected_output):
        assert Validator.checkAllowedCommands(command) == expected_output


    @pytest.mark.parametrize("tokens, expected_output", commandArgsParams)
    def test_check_command_args(self, tokens, expected_output):
        checkResult = Validator.checkCommandArgs(tokens)
        assert checkResult == expected_output