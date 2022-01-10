import pytest

from src.maximum_product_of_two_elements_in_an_array import Solution


@pytest.mark.parametrize(
    "nums,largest",
    [
        ([3, 4, 5, 2], 12),
        ([1, 5, 4, 5], 16),
        ([3, 7], 12),
    ],
)
def test_solution(nums, largest):
    assert Solution().maxProduct(nums) == largest
