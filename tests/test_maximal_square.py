import pytest

from src.maximal_square import Solution


@pytest.mark.parametrize(
    "matrix,expected_square",
    [
        (
            [
                ["1", "0", "1", "0", "0"],
                ["1", "0", "1", "1", "1"],
                ["1", "1", "1", "1", "1"],
                ["1", "0", "0", "1", "0"],
            ],
            4,
        ),
        ([["0", "1"], ["1", "0"]], 1),
        ([["0"]], 0),
    ],
)
def test_solution(matrix, expected_square):
    assert Solution().maximalSquare(matrix) == expected_square
