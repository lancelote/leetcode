import pytest

from src.maximum_score_from_performing_multiplication_operations import (
    Solution,
)


@pytest.mark.parametrize(
    "nums,multipliers,expected_score",
    [
        ([1, 2, 3], [3, 2, 1], 14),
        ([-5, -3, -3, -2, 7, 1], [-10, -5, 3, 4, 6], 102),
    ],
)
def test_solution(nums, multipliers, expected_score):
    assert Solution().maximumScore(nums, multipliers) == expected_score
