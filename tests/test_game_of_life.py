import pytest

from src.game_of_life import Solution


@pytest.mark.parametrize(
    "board,expected",
    (
        (
            [[0, 1, 0], [0, 0, 1], [1, 1, 1], [0, 0, 0]],
            [[0, 0, 0], [1, 0, 1], [0, 1, 1], [0, 1, 0]],
        ),
        ([[1, 1], [1, 0]], [[1, 1], [1, 1]]),
    ),
)
def test_solution(board, expected):
    Solution().gameOfLife(board)
    assert board == expected
