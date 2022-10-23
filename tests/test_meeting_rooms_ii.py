import pytest

from src.meeting_rooms_ii import Interval
from src.meeting_rooms_ii import Solution


@pytest.mark.parametrize(
    "intervals,expected",
    [
        ([Interval(0, 30), Interval(5, 10), Interval(15, 20)], 2),
        ([Interval(2, 7)], 1),
        ([Interval(1, 3), Interval(3, 4)], 1),
    ],
)
def test_solution(intervals, expected):
    assert Solution().min_meeting_rooms(intervals) == expected
