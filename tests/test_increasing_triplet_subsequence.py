import pytest

from src.increasing_triplet_subsequence import Solution


@pytest.mark.parametrize(
    "nums,expected",
    [
        ([1, 2, 3, 4, 5], True),
        ([5, 4, 3, 2, 1], False),
        ([2, 1, 5, 0, 4, 6], True),
    ],
)
def test_solution(nums, expected):
    assert Solution().increasingTriplet(nums) is expected
