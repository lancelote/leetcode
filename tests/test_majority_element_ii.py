import pytest

from src.majority_element_ii import Solution


@pytest.mark.parametrize(
    "nums,expected",
    (
        ([3, 2, 3], [3]),
        ([1], [1]),
        ([1, 2], [1, 2]),
        ([1, 2, 3], []),
    ),
)
def test_solution(nums, expected):
    assert Solution().majorityElement(nums) == expected
