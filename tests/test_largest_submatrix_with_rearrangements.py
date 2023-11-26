import pytest

from src.largest_submatrix_with_rearrangements import Solution


@pytest.mark.parametrize(
    "matrix,expected",
    (
        ([[0, 0, 1], [1, 1, 1], [1, 0, 1]], 4),
        ([[1, 0, 1, 0, 1]], 3),
        ([[1, 1, 0], [1, 0, 1]], 2),
    ),
)
def test_solution(matrix, expected):
    assert Solution().largestSubmatrix(matrix) == expected
