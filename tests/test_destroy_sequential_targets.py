import pytest

from src.destroy_sequential_targets import Solution


@pytest.mark.parametrize(
    "nums,space,expected",
    [
        ([3, 7, 8, 1, 1, 5], 2, 1),
        ([1, 3, 5, 2, 4, 6], 2, 1),
        ([6, 2, 5], 100, 2),
        ([2, 3, 4, 1, 4, 5, 3, 4, 5, 2], 10000, 4),
    ],
)
def test_solution(nums, space, expected):
    assert Solution().destroyTargets(nums, space) == expected
