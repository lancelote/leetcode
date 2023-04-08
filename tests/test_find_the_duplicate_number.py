import pytest

from src.find_the_duplicate_number import Solution


@pytest.mark.parametrize(
    "nums,expected",
    [
        ([1, 3, 4, 2, 2], 2),
        ([3, 1, 3, 4, 2], 3),
        ([2, 2, 2, 2, 2], 2),
    ],
)
def test_solution(nums, expected):
    assert Solution().findDuplicate(nums) == expected
