import pytest

from src.maximum_score_of_a_good_subarray import Solution


@pytest.mark.parametrize(
    "nums,k,expected",
    (
        ([1, 4, 3, 7, 4, 5], 3, 15),
        ([5, 5, 4, 5, 4, 1, 1, 1], 0, 20),
    ),
)
def test_solution(nums, k, expected):
    assert Solution().maximumScore(nums, k) == expected
