import pytest

from src.spiral_matrix import Solution


@pytest.mark.parametrize(
    "matrix,expected",
    [
        ([[1, 2, 3], [4, 5, 6], [7, 8, 9]], [1, 2, 3, 6, 9, 8, 7, 4, 5]),
        (
            [[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12]],
            [1, 2, 3, 4, 8, 12, 11, 10, 9, 5, 6, 7],
        ),
        ([[7], [9], [6]], [7, 9, 6]),
    ],
)
def test_solution(matrix, expected):
    assert Solution().spiralOrder(matrix) == expected
