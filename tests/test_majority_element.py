import pytest

from src.majority_element import Solution


@pytest.mark.parametrize(
    "nums,expected",
    (
        ([3, 2, 3], 3),
        ([2, 2, 1, 1, 1, 2, 2], 2),
    ),
)
def test_solution(nums, expected):
    assert Solution().majorityElement(nums) == expected
