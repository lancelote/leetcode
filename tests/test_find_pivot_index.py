import pytest

from src.find_pivot_index import Solution


@pytest.mark.parametrize(
    "nums,expected",
    (
        ([1, 7, 3, 6, 5, 6], 3),
        ([1, 2, 3], -1),
        ([2, 1, -1], 0),
    ),
)
def test_solution(nums, expected):
    assert Solution().pivotIndex(nums) == expected
