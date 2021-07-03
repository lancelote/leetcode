import pytest

from src.cyclically_rotating_a_grid import layer_coordinates
from src.cyclically_rotating_a_grid import Solution


@pytest.mark.parametrize(
    "layer_id,width,height,coordinates",
    [
        (
            0,
            4,
            6,
            [
                (0, 0),
                (1, 0),
                (2, 0),
                (3, 0),
                (3, 1),
                (3, 2),
                (3, 3),
                (3, 4),
                (3, 5),
                (2, 5),
                (1, 5),
                (0, 5),
                (0, 4),
                (0, 3),
                (0, 2),
                (0, 1),
            ],
        ),
        (
            1,
            4,
            6,
            [
                (1, 1),
                (2, 1),
                (2, 2),
                (2, 3),
                (2, 4),
                (1, 4),
                (1, 3),
                (1, 2),
            ],
        ),
    ],
)
def test_layer_coordinates(layer_id, width, height, coordinates):
    assert list(layer_coordinates(layer_id, width, height)) == coordinates


@pytest.mark.parametrize(
    "grid,k,expected",
    [
        ([[40, 10], [30, 20]], 1, [[10, 20], [40, 30]]),
        (
            [[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12], [13, 14, 15, 16]],
            2,
            [[3, 4, 8, 12], [2, 11, 10, 16], [1, 7, 6, 15], [5, 9, 13, 14]],
        ),
    ],
)
def test_solution(grid, k, expected):
    assert Solution().rotateGrid(grid, k) == expected
