import pytest

from src.integer_to_roman import Solution


@pytest.mark.parametrize(
    "num,expected",
    [
        (3, "III"),
        (4, "IV"),
        (5, "V"),
        (6, "VI"),
        (9, "IX"),
        (58, "LVIII"),
        (1994, "MCMXCIV"),
    ],
)
def test_solution(num, expected):
    assert Solution().intToRoman(num) == expected
