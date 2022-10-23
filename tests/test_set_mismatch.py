import pytest

from src.set_mismatch import Solution


@pytest.mark.parametrize(
    "nums,expected",
    [
        ([1, 2, 2, 4], [2, 3]),
        ([1, 1], [1, 2]),
        ([3, 2, 2], [2, 1]),
    ],
)
def test_solution(nums, expected):
    assert Solution().findErrorNums(nums) == expected
