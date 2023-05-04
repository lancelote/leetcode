import pytest

from src.sort_colors import Solution


@pytest.mark.parametrize(
    "nums,expected",
    [
        ([2, 0, 2, 1, 1, 0], [0, 0, 1, 1, 2, 2]),
        ([2, 0, 1], [0, 1, 2]),
    ],
)
def test_solution(nums, expected):
    Solution().sortColors(nums)
    assert nums == expected
