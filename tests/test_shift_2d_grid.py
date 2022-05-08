import pytest

from src.shift_2d_grid import Solution


@pytest.mark.parametrize(
    "grid,k,expected_grid",
    [
        (
            [[1, 2, 3], [4, 5, 6], [7, 8, 9]],
            1,
            [[9, 1, 2], [3, 4, 5], [6, 7, 8]],
        ),
        (
            [[3, 8, 1, 9], [19, 7, 2, 5], [4, 6, 11, 10], [12, 0, 21, 13]],
            4,
            [[12, 0, 21, 13], [3, 8, 1, 9], [19, 7, 2, 5], [4, 6, 11, 10]],
        ),
        (
            [[1, 2, 3], [4, 5, 6], [7, 8, 9]],
            9,
            [[1, 2, 3], [4, 5, 6], [7, 8, 9]],
        ),
    ],
)
def test_solution(grid, k, expected_grid):
    assert Solution().shiftGrid(grid, k) == expected_grid
