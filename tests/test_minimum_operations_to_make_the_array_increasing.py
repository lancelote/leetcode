import pytest

from src.minimum_operations_to_make_the_array_increasing import Solution


@pytest.mark.parametrize(
    "nums,total_operations_expected",
    [([1, 1, 1], 3), ([1, 5, 2, 4, 1], 14), ([8], 0)],
)
def test_solution(nums, total_operations_expected):
    assert Solution().minOperations(nums) == total_operations_expected
