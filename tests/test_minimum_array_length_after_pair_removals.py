import pytest

from src.minimum_array_length_after_pair_removals import Solution


@pytest.mark.parametrize(
    "nums,expected",
    (
        ([1, 3, 4, 9], 0),
        ([2, 3, 6, 9], 0),
        ([1, 1, 2], 1),
        ([1, 1], 2),
        ([2, 3, 4, 4, 4], 1),
        ([1, 4, 4, 9], 0),
        ([1, 1, 4, 4, 5, 5], 0),
    ),
)
def test_solution(nums, expected):
    assert Solution().minLengthAfterRemovals(nums) == expected
