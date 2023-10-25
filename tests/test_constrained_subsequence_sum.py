import pytest

from src.constrained_subsequence_sum import Solution


@pytest.mark.parametrize(
    "nums,k,expected",
    (
        ([10, 2, -10, 5, 20], 2, 37),
        ([-1, -2, -3], 1, -1),
        ([10, -2, -10, -5, 20], 2, 23),
    ),
)
def test_solution(nums, k, expected):
    assert Solution().constrainedSubsetSum(nums, k) == expected
