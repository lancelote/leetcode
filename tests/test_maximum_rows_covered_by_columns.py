import pytest

from src.maximum_rows_covered_by_columns import Solution


@pytest.mark.parametrize(
    "mat,cols,expected",
    [
        ([[0, 0, 0], [1, 0, 1], [0, 1, 1], [0, 0, 1]], 2, 3),
        ([[1], [0]], 1, 2),
    ],
)
def test_solution(mat, cols, expected):
    assert Solution().maximumRows(mat, cols) == expected
