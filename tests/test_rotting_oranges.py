import pytest

from src.rotting_oranges import Solution


@pytest.mark.parametrize(
    "grid,expected",
    (
        ([[2, 1, 1], [1, 1, 0], [0, 1, 1]], 4),
        ([[2, 1, 1], [0, 1, 1], [1, 0, 1]], -1),
        ([[0, 2]], 0),
        ([[0]], 0),
    ),
)
def test_solution(grid, expected):
    assert Solution().orangesRotting(grid) == expected
