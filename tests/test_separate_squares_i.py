import pytest

from src.separate_squares_i import ALPHA
from src.separate_squares_i import Solution


@pytest.mark.parametrize(
    "squares,expected",
    (
        ([[0, 0, 1], [2, 2, 1]], 1.0),
        ([[0, 0, 2], [1, 1, 1]], 1.16667),
    ),
)
def test_solution(squares, expected):
    assert Solution().separateSquares(squares) == pytest.approx(expected, rel=ALPHA)
