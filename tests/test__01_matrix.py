import pytest

from src._01_matrix import Solution


@pytest.mark.parametrize(
    "mat,expected",
    (
        ([[0, 1], [1, 1]], [[0, 1], [1, 2]]),
        ([[0, 0, 0], [0, 1, 0], [0, 0, 0]], [[0, 0, 0], [0, 1, 0], [0, 0, 0]]),
        ([[0, 0, 0], [0, 1, 0], [1, 1, 1]], [[0, 0, 0], [0, 1, 0], [1, 2, 1]]),
    ),
)
def test_solution(mat, expected):
    assert Solution().updateMatrix(mat) == expected
