import pytest

from src.non_overlapping_intervals import Solution


@pytest.mark.parametrize(
    "intervals,expected",
    [
        ([[1, 2], [2, 3], [3, 4], [1, 3]], 1),
        ([[1, 2], [1, 2], [1, 2]], 2),
        ([[1, 2], [2, 3]], 0),
        ([[0, 2], [1, 3], [2, 4], [3, 5], [4, 6]], 2),
    ],
)
def test_solution(intervals, expected):
    assert Solution().eraseOverlapIntervals(intervals) == expected
