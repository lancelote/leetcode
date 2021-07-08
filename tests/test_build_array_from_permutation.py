import pytest

from src.build_array_from_permutation import Solution


@pytest.mark.parametrize(
    "nums,expected",
    [
        ([0, 2, 1, 5, 3, 4], [0, 1, 2, 4, 5, 3]),
        ([5, 0, 1, 2, 3, 4], [4, 5, 0, 1, 2, 3]),
    ],
)
def test_solution(nums, expected):
    assert Solution().buildArray(nums) == expected
