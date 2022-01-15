import pytest

from src.binary_search import Solution


@pytest.mark.parametrize(
    "nums,target,expected",
    [
        ([-1, 0, 3, 5, 9, 12], 9, 4),
        ([-1, 0, 3, 5, 9, 12], 2, -1),
        ([1, 2, 3], 1, 0),
        ([1, 2, 3], 3, 2),
        ([1, 2, 3, 4], 1, 0),
        ([1, 2, 3, 4], 4, 3),
    ],
)
def test_solution(nums, target, expected):
    assert Solution().search(nums, target) == expected
