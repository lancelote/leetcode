import pytest

from src.count_nice_pairs_in_an_array import Solution


@pytest.mark.parametrize(
    "nums,expected",
    (
        ([42, 11, 1, 97], 2),
        ([13, 10, 35, 24, 76], 4),
    ),
)
def test_solution(nums, expected):
    assert Solution().countNicePairs(nums) == expected
