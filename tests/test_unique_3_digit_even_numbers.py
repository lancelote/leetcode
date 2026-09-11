import pytest

from src.unique_3_digit_even_numbers import Solution


@pytest.mark.parametrize(
    "digits,expected",
    (
        ([1, 2, 3, 4], 12),
        ([0, 2, 2], 2),
        ([6, 6, 6], 1),
        ([1, 3, 5], 0),
    ),
)
def test_solution(digits, expected):
    assert Solution().totalNumbers(digits) == expected
