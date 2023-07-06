import pytest

from src.subsets import Solution


@pytest.mark.parametrize(
    "nums,expected",
    (
        ([1, 2, 3], [[], [3], [2], [2, 3], [1], [1, 3], [1, 2], [1, 2, 3]]),
        ([0], [[], [0]]),
    ),
)
def test_solution(nums, expected):
    assert Solution().subsets(nums) == expected
