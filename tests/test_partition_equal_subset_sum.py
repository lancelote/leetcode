import pytest

from src.partition_equal_subset_sum import Solution


@pytest.mark.parametrize(
    "nums,expected",
    (
        ([1, 5, 11, 5], True),
        ([1, 2, 3, 5], False),
    ),
)
def test_solution(nums, expected):
    assert Solution().canPartition(nums) is expected
