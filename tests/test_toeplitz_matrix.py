import pytest

from src.toeplitz_matrix import Solution


@pytest.mark.parametrize(
    "matrix,expected",
    [
        ([[1, 2, 3, 4], [5, 1, 2, 3], [9, 5, 1, 2]], True),
        ([[1, 2], [2, 2]], False),
    ],
)
def test_solution(matrix, expected):
    assert Solution().isToeplitzMatrix(matrix) is expected
