import pytest

from src.difference_between_element_sum_and_digit_sum_of_an_array import (
    Solution,
)


@pytest.mark.parametrize(
    "nums,expected",
    [
        ([1, 15, 6, 3], 9),
        ([1, 2, 3, 4], 0),
    ],
)
def test_solution(nums, expected):
    assert Solution().differenceOfSum(nums) == expected
