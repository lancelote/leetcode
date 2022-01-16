import pytest

from src.search_insert_position import Solution


@pytest.mark.parametrize(
    "nums,target,expected",
    [
        ([1, 3, 5, 6], 5, 2),
        ([1, 3, 5, 6], 2, 1),
        ([1, 3, 5, 6], 7, 4),
    ],
)
def test_solution(nums, target, expected):
    assert Solution().searchInsert(nums, target) == expected
