import pytest

from src.count_the_digits_that_divide_a_number import Solution


@pytest.mark.parametrize(
    "num,expected",
    [
        (7, 1),
        (121, 2),
        (1248, 4),
    ],
)
def test_solution(num, expected):
    assert Solution().countDigits(num) == expected
