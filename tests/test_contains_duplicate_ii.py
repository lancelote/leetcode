import pytest

from src.contains_duplicate_ii import Solution


@pytest.mark.parametrize(
    "nums,k,expected",
    [
        ([1, 2, 3, 1], 3, True),
        ([1, 0, 1, 1], 1, True),
        ([1, 2, 3, 1, 2, 3], 2, False),
        ([1, 2, 1], 0, False),
        ([1, 2, 3, 4, 5, 6, 7, 8, 9, 10], 15, False),
    ],
)
def test_solution(nums, k, expected):
    assert Solution().containsNearbyDuplicate(nums, k) is expected
