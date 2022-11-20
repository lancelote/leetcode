import pytest

from src.basic_calculator import Solution


@pytest.mark.parametrize(
    "s,expected",
    [
        ("1 + 1", 2),
        (" 2-1 + 2 ", 3),
        ("(1+(4+5+2)-3)+(6+8)", 23),
    ],
)
def test_solution(s, expected):
    assert Solution().calculate(s) == expected
