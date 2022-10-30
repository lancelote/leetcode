import pytest

from src.shortest_path_in_a_grid_with_obstacles_elimination import Solution


@pytest.mark.parametrize(
    "grid,k,expected",
    [
        ([[0, 0, 0], [1, 1, 0], [0, 0, 0], [0, 1, 1], [0, 0, 0]], 1, 6),
        ([[0, 1], [1, 0]], 1, 2),
        (
            [
                [0, 0],
                [0, 1],
                [0, 0],
            ],
            0,
            3,
        ),
        ([[0, 1, 1], [1, 1, 1], [1, 0, 0]], 1, -1),
        (
            [
                [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                [0, 1, 1, 1, 1, 1, 1, 1, 1, 0],
                [0, 1, 0, 0, 0, 0, 0, 0, 0, 0],
                [0, 1, 0, 1, 1, 1, 1, 1, 1, 1],
                [0, 1, 0, 0, 0, 0, 0, 0, 0, 0],
                [0, 1, 1, 1, 1, 1, 1, 1, 1, 0],
                [0, 1, 0, 0, 0, 0, 0, 0, 0, 0],
                [0, 1, 0, 1, 1, 1, 1, 1, 1, 1],
                [0, 1, 0, 1, 1, 1, 1, 0, 0, 0],
                [0, 1, 0, 0, 0, 0, 0, 0, 1, 0],
                [0, 1, 1, 1, 1, 1, 1, 0, 1, 0],
                [0, 0, 0, 0, 0, 0, 0, 0, 1, 0],
            ],
            1,
            20,
        ),
        (
            [
                [0, 0],
                [1, 0],
                [1, 0],
                [1, 0],
                [1, 0],
                [1, 0],
                [0, 0],
                [0, 1],
                [0, 1],
                [0, 1],
                [0, 0],
                [1, 0],
                [1, 0],
                [0, 0],
            ],
            4,
            14,
        ),
    ],
)
def test_solution(grid, k, expected):
    assert Solution().shortestPath(grid, k) == expected
