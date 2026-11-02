import pytest

from src.aggregate_two_time_series import Solution


@pytest.mark.parametrize(
    "series1,series2,expected",
    (
        ([[1, 3], [4, 1]], [[2, 2], [5, 2]], [[1, 5], [2, 3], [4, 3], [5, 2]]),
        ([[1, 5], [3, 1]], [[2, 2]], [[1, 7], [2, 3], [3, 1]]),
        ([[1, 5]], [[1000000000, 2]], [[1, 7], [1000000000, 2]]),
    ),
)
def test_solution(series1, series2, expected):
    assert Solution().aggregateTimeSeries(series1, series2) == expected
