import pytest

from src.set_matrix_zeroes import Solution


@pytest.mark.parametrize(
    "matrix,expected",
    [
        ([[1, 1, 1], [1, 0, 1], [1, 1, 1]], [[1, 0, 1], [0, 0, 0], [1, 0, 1]]),
        (
            [[0, 1, 2, 0], [3, 4, 5, 2], [1, 3, 1, 5]],
            [[0, 0, 0, 0], [0, 4, 5, 0], [0, 3, 1, 0]],
        ),
        ([[1, 0]], [[0, 0]]),
        (
            [
                [0, 0, 0, 5],
                [4, 3, 1, 4],
                [0, 1, 1, 4],
                [1, 2, 1, 3],
                [0, 0, 1, 1],
            ],
            [
                [0, 0, 0, 0],
                [0, 0, 0, 4],
                [0, 0, 0, 0],
                [0, 0, 0, 3],
                [0, 0, 0, 0],
            ],
        ),
    ],
)
def test_solution(matrix, expected):
    Solution().setZeroes(matrix)
    assert matrix == expected
