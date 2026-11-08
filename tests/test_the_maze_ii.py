import pytest

from src.the_maze_ii import Solution


@pytest.mark.parametrize(
    "maze,start,destination,expected",
    (
        (
            [
                [0, 0, 1, 0, 0],
                [0, 0, 0, 0, 0],
                [0, 0, 0, 1, 0],
                [1, 1, 0, 1, 1],
                [0, 0, 0, 0, 0],
            ],
            [0, 4],
            [4, 4],
            12,
        ),
        (
            [
                [0, 0, 1, 0, 0],
                [0, 0, 0, 0, 0],
                [0, 0, 0, 1, 0],
                [1, 1, 0, 1, 1],
                [0, 0, 0, 0, 0],
            ],
            [0, 4],
            [3, 2],
            -1,
        ),
        (
            [
                [0, 0, 0, 0, 0],
                [1, 1, 0, 0, 1],
                [0, 0, 0, 0, 0],
                [0, 1, 0, 0, 1],
                [0, 1, 0, 0, 0],
            ],
            [4, 3],
            [0, 1],
            -1,
        ),
    ),
)
def test_solution(maze, start, destination, expected):
    assert Solution().shortestDistance(maze, start, destination) == expected
