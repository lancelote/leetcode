import pytest
from src.maximum_product_difference_between_two_pairs import Solution


@pytest.mark.parametrize(
    "nums,max_sum",
    [
        ([5, 6, 2, 7, 4], 34),
        ([4, 2, 5, 9, 7, 4, 8], 64),
    ],
)
def test_solution(nums, max_sum):
    assert Solution().maxProductDifference(nums) == max_sum
