import pytest

from src.path_with_maximum_minimum_value import Solution


@pytest.mark.parametrize(
    "grid,expected",
    (
        ([[5, 4, 5], [1, 2, 6], [7, 4, 6]], 4),
        ([[2, 2, 1, 2, 2, 2], [1, 2, 2, 2, 1, 2]], 2),
        (
            [
                [3, 4, 6, 3, 4],
                [0, 2, 1, 1, 7],
                [8, 8, 3, 2, 7],
                [3, 2, 4, 9, 8],
                [4, 1, 2, 0, 0],
                [4, 6, 5, 4, 3],
            ],
            3,
        ),
    ),
)
def test_solution(grid, expected):
    assert Solution().maximumMinimumPath(grid) == expected
