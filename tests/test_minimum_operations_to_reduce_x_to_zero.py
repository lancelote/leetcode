import pytest

from src.minimum_operations_to_reduce_x_to_zero import Solution


@pytest.mark.parametrize(
    "nums,x,expected",
    (
        ([1, 1, 4, 2, 3], 5, 2),
        ([5, 6, 7, 8, 9], 4, -1),
        ([3, 2, 20, 1, 1, 3], 10, 5),
        ([5, 2, 3, 1, 1], 5, 1),
    ),
)
def test_solution(nums, x, expected):
    assert Solution().minOperations(nums, x) == expected
