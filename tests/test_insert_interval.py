import pytest

from src.insert_interval import Solution


@pytest.mark.parametrize(
    "intervals,new_interval,expected",
    [
        ([[1, 3], [6, 9]], [2, 5], [[1, 5], [6, 9]]),
        (
            [[1, 2], [3, 5], [6, 7], [8, 10], [12, 16]],
            [4, 8],
            [[1, 2], [3, 10], [12, 16]],
        ),
        ([[1, 5]], [2, 3], [[1, 5]]),
    ],
)
def test_solution(intervals, new_interval, expected):
    assert Solution().insert(intervals, new_interval) == expected
