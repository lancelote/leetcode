import pytest

from src.minimum_number_of_operations_to_make_array_continuous import Solution


@pytest.mark.parametrize(
    "nums,expected",
    (
        ([4, 2, 5, 3], 0),
        ([1, 2, 3, 5, 6], 1),
        ([1, 10, 100, 1000], 3),
        ([8, 5, 9, 9, 8, 4], 2),
    ),
)
def test_solution(nums, expected):
    assert Solution().minOperations(nums) == expected
