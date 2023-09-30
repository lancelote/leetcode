import pytest

from src.minimum_operations_to_collect_elements import Solution


@pytest.mark.parametrize(
    "nums,k,expected",
    (
        ([3, 1, 5, 4, 2], 2, 4),
        ([3, 1, 5, 4, 2], 5, 5),
        ([3, 2, 5, 3, 1], 3, 4),
    ),
)
def test_solution(nums, k, expected):
    assert Solution().minOperations(nums, k) == expected
