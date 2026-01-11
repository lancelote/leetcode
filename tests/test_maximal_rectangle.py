import pytest

from src.maximal_rectangle import Solution


@pytest.mark.parametrize(
    "matrix,expected",
    (
        (
            [
                ["1", "0", "1", "0", "0"],
                ["1", "0", "1", "1", "1"],
                ["1", "1", "1", "1", "1"],
                ["1", "0", "0", "1", "0"],
            ],
            6,
        ),
        ([["0"]], 0),
        ([["1"]], 1),
    ),
)
def test_solution(matrix, expected):
    assert Solution().maximalRectangle(matrix) == expected
