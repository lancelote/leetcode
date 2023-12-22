import pytest

from src.shortest_path_in_binary_matrix import Solution


@pytest.mark.parametrize(
    "grid,expected",
    (
        ([[0, 1], [1, 0]], 2),
        ([[0, 0, 0], [1, 1, 0], [1, 1, 0]], 4),
        ([[1, 0, 0], [1, 1, 0], [1, 1, 0]], -1),
    ),
)
def test_solution(grid, expected):
    assert Solution().shortestPathBinaryMatrix(grid) == expected
