import pytest

from src.roman_to_integer import Solution


@pytest.mark.parametrize(
    "roman,integer",
    [
        ("III", 3),
        ("IV", 4),
        ("IX", 9),
        ("LVIII", 58),
        ("MCMXCIV", 1994),
    ],
)
def test_solution(roman, integer):
    assert Solution().romanToInt(roman) == integer
