import pytest

from src.count_days_spent_together import Solution


@pytest.mark.parametrize(
    "aa,la,ab,lb,expected",
    [
        ("08-15", "08-18", "08-16", "08-19", 3),
        ("10-01", "10-31", "11-01", "12-31", 0),
        ("09-01", "10-19", "06-19", "10-20", 49),
    ],
)
def test_solution(aa, la, ab, lb, expected):
    assert Solution().countDaysTogether(aa, la, ab, lb) == expected
