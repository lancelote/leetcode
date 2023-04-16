import pytest

from src.left_and_right_sum_differences import Solution


@pytest.mark.parametrize(
    "nums,expected",
    [
        ([10, 4, 8, 3], [15, 1, 11, 22]),
        ([1], [0]),
    ],
)
def test_solution(nums, expected):
    assert Solution().leftRigthDifference(nums) == expected
