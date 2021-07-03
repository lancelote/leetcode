import pytest

from src.how_many_numbers_are_smaller_than_the_current_number import Solution


@pytest.mark.parametrize(
    "nums,expected",
    [
        ([8, 1, 2, 2, 3], [4, 0, 1, 1, 3]),
        ([6, 5, 4, 8], [2, 1, 0, 3]),
        ([7, 7, 7, 7], [0, 0, 0, 0]),
    ],
)
def test_solution(nums, expected):
    assert Solution().smallerNumbersThanCurrent(nums) == expected
