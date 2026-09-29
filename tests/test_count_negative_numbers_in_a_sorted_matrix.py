import pytest

from src.count_negative_numbers_in_a_sorted_matrix import Solution


@pytest.mark.parametrize(
    "grid,expected",
    (
        ([[4, 3, 2, -1], [3, 2, 1, -1], [1, 1, -1, -2], [-1, -1, -2, -3]], 8),
        ([[3, 2], [1, 0]], 0),
    ),
)
def test_solution(grid, expected):
    assert Solution().countNegatives(grid) == expected
