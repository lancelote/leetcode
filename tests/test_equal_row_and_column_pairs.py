import pytest

from src.equal_row_and_column_pairs import Solution


@pytest.mark.parametrize(
    "grid,expected",
    (
        ([[3, 2, 1], [1, 7, 6], [2, 7, 7]], 1),
        ([[3, 1, 2, 2], [1, 4, 4, 5], [2, 4, 2, 2], [2, 4, 2, 2]], 3),
    ),
)
def test_solution(grid, expected):
    assert Solution().equalPairs(grid) == expected
