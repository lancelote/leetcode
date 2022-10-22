import pytest

from src.meeting_rooms import Interval
from src.meeting_rooms import Solution


@pytest.mark.parametrize(
    "intervals,expected",
    [
        ([], True),
        ([Interval(0, 30), Interval(5, 10), Interval(15, 20)], False),
        ([Interval(5, 9), Interval(9, 15)], True),
    ],
)
def test_solution(intervals, expected):
    assert Solution().can_attend_meetings(intervals) is expected
