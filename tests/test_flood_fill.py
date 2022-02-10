import pytest

from src.flood_fill import Solution


@pytest.mark.parametrize(
    "image,y,x,new_color,expected",
    [
        (
            [[1, 1, 1], [1, 1, 0], [1, 0, 1]],
            1,
            1,
            2,
            [[2, 2, 2], [2, 2, 0], [2, 0, 1]],
        ),
        ([[0, 0, 0], [0, 0, 0]], 0, 0, 2, [[2, 2, 2], [2, 2, 2]]),
        ([[0, 0, 0], [0, 1, 1]], 1, 1, 1, [[0, 0, 0], [0, 1, 1]]),
    ],
)
def test_solution(image, y, x, new_color, expected):
    Solution().floodFill(image, y, x, new_color)
    assert image == expected
