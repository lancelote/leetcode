import pytest

from src.sort_an_array import Solution


@pytest.mark.parametrize(
    "nums,expected",
    [
        ([5, 2, 3, 1], [1, 2, 3, 5]),
        ([5, 1, 1, 2, 0, 0], [0, 0, 1, 1, 2, 5]),
    ],
)
def test_solution(nums, expected):
    assert Solution().sortArray(nums) == expected
