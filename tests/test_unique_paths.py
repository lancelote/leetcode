import pytest

from src.unique_paths import Solution


@pytest.mark.parametrize(
    "rows,cols,expected",
    [
        (3, 7, 28),
        (3, 2, 3),
    ],
)
def test_solution(rows, cols, expected):
    assert Solution().uniquePaths(rows, cols) == expected
