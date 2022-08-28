import pytest

from src.max_sum_of_rectangle_no_larger_than_k import Solution


@pytest.mark.parametrize(
    "matrix,k,expected_sum",
    [
        ([[1, 0, 1], [0, -2, 3]], 2, 2),
        ([[2, 2, -1]], 3, 3),
        ([[2, 2, -1]], 0, -1),
        ([[5, -4, -3, 4], [-3, -4, 4, 5], [5, 1, 5, -4]], 10, 10),
    ],
)
def test_solution(matrix, k, expected_sum):
    assert Solution().maxSumSubmatrix(matrix, k) == expected_sum
