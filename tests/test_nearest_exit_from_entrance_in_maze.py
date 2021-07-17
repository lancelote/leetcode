import pytest

from src.nearest_exit_from_entrance_in_maze import Solution


@pytest.mark.parametrize(
    "maze,entrance,steps",
    [
        (
            [["+", "+", ".", "+"], [".", ".", ".", "+"], ["+", "+", "+", "."]],
            [1, 2],
            1,
        ),
        (
            [["+", "+", "+"], [".", ".", "."], ["+", "+", "+"]],
            [1, 0],
            2,
        ),
        ([[".", "+"]], [0, 0], -1),
    ],
)
def test_solution(maze, entrance, steps):
    assert Solution().nearestExit(maze, entrance) == steps
