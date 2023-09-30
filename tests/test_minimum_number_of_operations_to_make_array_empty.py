import pytest

from src.minimum_number_of_operations_to_make_array_empty import Solution


@pytest.mark.parametrize(
    "nums,expected",
    (
        ([2, 3, 3, 2, 2, 4, 2, 3, 4], 4),
        ([2, 1, 2, 2, 3, 3], -1),
    ),
)
def test_solution(nums, expected):
    assert Solution().minOperations(nums) == expected
