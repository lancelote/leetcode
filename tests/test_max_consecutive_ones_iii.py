import pytest

from src.max_consecutive_ones_iii import Solution


@pytest.mark.parametrize(
    "nums,k,expected",
    (
        ([1, 1, 1, 0, 0, 0, 1, 1, 1, 1, 0], 2, 6),
        ([0, 0, 1, 1, 0, 0, 1, 1, 1, 0, 1, 1, 0, 0, 0, 1, 1, 1, 1], 3, 10),
    ),
)
def test_solution(nums, k, expected):
    assert Solution().longestOnes(nums, k) == expected
