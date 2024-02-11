import pytest

from src.string_to_integer_atoi import Solution


@pytest.mark.parametrize(
    "s,expected",
    (
        ("42", 42),
        ("   -42", -42),
        ("4193 with words", 4193),
        ("words and 987", 0),
    ),
)
def test_solution(s, expected):
    assert Solution().myAtoi(s) == expected
