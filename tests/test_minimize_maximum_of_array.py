import pytest

from src.minimize_maximum_of_array import Solution


@pytest.mark.parametrize(
    "nums,expected",
    [
        ([3, 7, 1, 6], 5),
        ([10, 1], 10),
        ([13, 13, 20, 0, 8, 9, 9], 16),
        ([6, 9, 3, 8, 14], 8),
    ],
)
def test_solution(nums, expected):
    assert Solution().minimizeArrayValue(nums) == expected
