import pytest

from src.maximum_count_of_positive_integer_and_negative_integer import Solution


@pytest.mark.parametrize(
    "nums,expected",
    [
        ([-2, -1, -1, 1, 2, 3], 3),
        ([-3, -2, -1, 0, 0, 1, 2], 3),
        ([5, 20, 66, 1314], 4),
    ],
)
def test_solution(nums, expected):
    assert Solution().maximumCount(nums) == expected
