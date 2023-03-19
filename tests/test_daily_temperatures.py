import pytest

from src.daily_temperatures import Solution


@pytest.mark.parametrize(
    "temperatures,expected",
    [
        ([73, 74, 75, 71, 69, 72, 76, 73], [1, 1, 4, 2, 1, 1, 0, 0]),
        ([30, 40, 50, 60], [1, 1, 1, 0]),
        ([30, 60, 90], [1, 1, 0]),
    ],
)
def test_solution(temperatures, expected):
    assert Solution().dailyTemperatures(temperatures) == expected
