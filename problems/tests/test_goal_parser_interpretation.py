import pytest
from src.goal_parser_interpretation import Solution


@pytest.mark.parametrize(
    "command,parsed_str",
    [
        ("G()(al)", "Goal"),
        ("G()()()()(al)", "Gooooal"),
    ],
)
def test_solution(command, parsed_str):
    assert Solution().interpret(command) == parsed_str
