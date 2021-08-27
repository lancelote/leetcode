import pytest

from src.find_greatest_common_divisor_of_array import Solution


@pytest.mark.parametrize(
    "nums,expected",
    [
        ([2, 5, 6, 9, 10], 2),
        ([7, 5, 6, 8, 3], 1),
        ([3, 3], 3),
    ],
)
def test_solution(nums, expected):
    assert Solution().findGCD(nums) == expected
