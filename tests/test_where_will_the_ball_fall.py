import pytest

from src.where_will_the_ball_fall import Solution


@pytest.mark.parametrize(
    "grid,expected",
    [
        (
            [
                [1, 1, 1, -1, -1],
                [1, 1, 1, -1, -1],
                [-1, -1, -1, 1, 1],
                [1, 1, 1, 1, -1],
                [-1, -1, -1, -1, -1],
            ],
            [1, -1, -1, -1, -1],
        ),
        ([[-1]], [-1]),
        (
            [
                [1, 1, 1, 1, 1, 1],
                [-1, -1, -1, -1, -1, -1],
                [1, 1, 1, 1, 1, 1],
                [-1, -1, -1, -1, -1, -1],
            ],
            [0, 1, 2, 3, 4, -1],
        ),
    ],
)
def test_solution(grid, expected):
    assert Solution().findBall(grid) == expected
