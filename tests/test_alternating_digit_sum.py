import pytest

from src.alternating_digit_sum import Solution


@pytest.mark.parametrize(
    "n,expected",
    [
        (521, 4),
        (111, 1),
        (886996, 0),
    ],
)
def test_solution(n, expected):
    assert Solution().alternateDigitSum(n) == expected
