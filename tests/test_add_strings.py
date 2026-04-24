import pytest

from src.add_strings import Solution


@pytest.mark.parametrize(
    "num1,num2,expected",
    (
        ("11", "123", "134"),
        ("456", "77", "533"),
        ("0", "0", "0"),
    ),
)
def test_solution(num1, num2, expected):
    assert Solution().addStrings(num1, num2) == expected
