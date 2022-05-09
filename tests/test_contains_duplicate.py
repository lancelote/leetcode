import pytest

from src.contains_duplicate import Solution


@pytest.mark.parametrize(
    "nums,expected",
    [
        ([1, 2, 3, 1], True),
        ([1, 2, 3, 4], False),
        ([1, 1, 1, 3, 3, 4, 3, 2, 4, 2], True),
    ],
)
def test_solution(nums, expected):
    assert Solution().containsDuplicate(nums) == expected
