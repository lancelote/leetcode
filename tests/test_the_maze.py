import pytest

from src.the_maze import Solution


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
            True,
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
            False,
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
            False,
        ),
    ),
)
def test_solution(maze, start, destination, expected):
    assert Solution().hasPath(maze, start, destination) is expected
