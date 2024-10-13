import pytest

from src.missing_ranges import Solution


@pytest.mark.parametrize(
    "nums,lower,upper,expected",
    (
        ([0, 1, 3, 50, 75], 0, 99, [[2, 2], [4, 49], [51, 74], [76, 99]]),
        ([-1], -1, -1, []),
        ([], 1, 1, [[1, 1]]),
        ([-1], -1, 0, [[0, 0]]),
    ),
)
def test_solution(nums, lower, upper, expected):
    assert Solution().findMissingRanges(nums, lower, upper) == expected
