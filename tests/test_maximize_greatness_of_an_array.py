import pytest

from src.maximize_greatness_of_an_array import Solution


@pytest.mark.parametrize(
    "nums,expected",
    [
        ([1, 3, 5, 2, 1, 3, 1], 4),
        ([1, 2, 3, 4], 3),
    ],
)
def test_solution(nums, expected):
    assert Solution().maximizeGreatness(nums) == expected
