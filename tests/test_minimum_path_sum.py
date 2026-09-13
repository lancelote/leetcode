import pytest

from src.minimum_path_sum import Solution


@pytest.mark.parametrize(
    "grid,expected",
    (
        ([[1, 3, 1], [1, 5, 1], [4, 2, 1]], 7),
        ([[1, 2, 3], [4, 5, 6]], 12),
    ),
)
def test_solution(grid, expected):
    assert Solution().minPathSum(grid) == expected
