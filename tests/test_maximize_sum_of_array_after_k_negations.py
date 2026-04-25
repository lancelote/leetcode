import pytest

from src.maximize_sum_of_array_after_k_negations import Solution


@pytest.mark.parametrize(
    "nums,k,expected",
    (
        ([4, 2, 3], 1, 5),
        ([3, -1, 0, 2], 3, 6),
        ([2, -3, -1, 5, -4], 2, 13),
    ),
)
def test_solution(nums, k, expected):
    assert Solution().largestSumAfterKNegations(nums, k) == expected
