import pytest

from src._4sum_ii import Solution


@pytest.mark.parametrize(
    "arrays,expected",
    [
        (([1, 2], [-2, -1], [-1, 2], [0, 2]), 2),
        (([0], [0], [0], [0]), 1),
    ],
)
def test_solution(arrays, expected):
    assert Solution().fourSumCount(*arrays) == expected
