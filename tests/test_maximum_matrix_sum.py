import pytest

from src.maximum_matrix_sum import Solution


@pytest.mark.parametrize(
    "matrix,result",
    [
        ([[1, -1], [-1, 1]], 4),
        ([[1, 2, 3], [-1, -2, -3], [1, 2, 3]], 16),
        ([[-1, 0, -1], [-2, 1, 3], [3, 2, 2]], 15),
        ([[2, 9, 3], [5, 4, -4], [1, 7, 1]], 34),
    ],
)
def test_solution(matrix, result):
    assert Solution().maxMatrixSum(matrix) == result
