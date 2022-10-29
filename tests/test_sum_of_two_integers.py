import pytest

from src.sum_of_two_integers import Solution


@pytest.mark.parametrize(
    "a,b,expected",
    [
        (1, 2, 3),
        (2, 3, 5),
        (-1, 1, 0),
        (-12, -8, -20),
    ],
)
def test_solution(a, b, expected):
    assert Solution().getSum(a, b) == expected
