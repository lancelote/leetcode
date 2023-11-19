import pytest

from src.reduction_operations_to_make_the_array_elements_equal import Solution


@pytest.mark.parametrize(
    "nums,expected",
    (
        ([5, 1, 3], 3),
        ([1, 1, 1], 0),
        ([1, 1, 2, 2, 3], 4),
    ),
)
def test_solution(nums, expected):
    assert Solution().reductionOperations(nums) == expected
