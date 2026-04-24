import pytest

from src.meeting_rooms import Solution


@pytest.mark.parametrize(
    "intervals,expected",
    [
        ([], True),
        ([[0, 30], [5, 10], [15, 20]], False),
        ([[5, 9], [9, 15]], True),
    ],
)
def test_solution(intervals, expected):
    assert Solution().canAttendMeetings(intervals) is expected
