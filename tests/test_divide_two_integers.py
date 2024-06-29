import pytest

from src.divide_two_integers import Solution


@pytest.mark.parametrize(
    "dividend,divisor,expected",
    (
        (10, 3, 3),
        (7, -3, -2),
        (-2147483648, -1, 2147483647),
        (2147483647, 1, 2147483647),
    ),
)
def test_solution(dividend, divisor, expected):
    assert Solution().divide(dividend, divisor) == expected
