import pytest

from src.search_a_2d_matrix import Solution


@pytest.mark.parametrize(
    "matrix,target,expected",
    [
        ([[1, 3, 5, 7], [10, 11, 16, 20], [23, 30, 34, 60]], 3, True),
        ([[1, 3, 5, 7], [10, 11, 16, 20], [23, 30, 34, 60]], 13, False),
        ([[1, 3, 5, 7], [10, 11, 16, 20], [23, 30, 34, 50]], 11, True),
        ([[1]], 2, False),
    ],
)
def test_solution(matrix, target, expected):
    assert Solution().searchMatrix(matrix, target) is expected
