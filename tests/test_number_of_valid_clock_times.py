import pytest

from src.number_of_valid_clock_times import Solution


@pytest.mark.parametrize(
    "time,expected",
    [
        ("?5:00", 2),
        ("0?:0?", 100),
        ("??:??", 1440),
        ("2?:??", 240),
    ],
)
def test_solution(time, expected):
    assert Solution().countTime(time) == expected
