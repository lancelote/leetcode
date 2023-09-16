import pytest

from src.path_with_minimum_effort import Solution


@pytest.mark.parametrize(
    "heights,expected",
    (
        ([[1, 2, 2], [3, 8, 2], [5, 3, 5]], 2),
        ([[1, 2, 3], [3, 8, 4], [5, 3, 5]], 1),
        (
            [
                [1, 2, 1, 1, 1],
                [1, 2, 1, 2, 1],
                [1, 2, 1, 2, 1],
                [1, 2, 1, 2, 1],
                [1, 1, 1, 2, 1],
            ],
            0,
        ),
    ),
)
def test_solution(heights, expected):
    assert Solution().minimumEffortPath(heights) == expected
