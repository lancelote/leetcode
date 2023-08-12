import pytest

from src.unique_paths_ii import Solution


@pytest.mark.parametrize(
    "grid,expected",
    (
        ([[0, 0, 0], [0, 1, 0], [0, 0, 0]], 2),
        ([[0, 1], [0, 0]], 1),
        ([[0, 0], [0, 1]], 0),
        ([[0, 0], [1, 1], [0, 0]], 0),
    ),
)
def test_solution(grid, expected):
    assert Solution().uniquePathsWithObstacles(grid) == expected
