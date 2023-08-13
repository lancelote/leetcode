import pytest

from src.check_if_there_is_a_valid_partition_for_the_array import Solution


@pytest.mark.parametrize(
    "nums,expected",
    (
        ([4, 4, 4, 5, 6], True),
        ([1, 1, 1, 2], False),
    ),
)
def test_solution(nums, expected):
    assert Solution().validPartition(nums) is expected
