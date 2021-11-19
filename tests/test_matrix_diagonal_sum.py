import pytest

from src.matrix_diagonal_sum import Solution


@pytest.mark.parametrize(
    "matrix,expected_sum",
    [
        ([[1, 2, 3], [4, 5, 6], [7, 8, 9]], 25),
        ([[1, 1, 1, 1], [1, 1, 1, 1], [1, 1, 1, 1], [1, 1, 1, 1]], 8),
        ([[5]], 5),
    ],
)
def test_solution(matrix, expected_sum):
    assert Solution().diagonalSum(matrix) == expected_sum
