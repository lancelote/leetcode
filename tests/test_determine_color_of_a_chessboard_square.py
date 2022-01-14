import pytest

from src.determine_color_of_a_chessboard_square import Solution


@pytest.mark.parametrize(
    "coordinates,expected",
    [
        ("a1", False),
        ("h3", True),
        ("c7", False),
    ],
)
def test_solution(coordinates, expected):
    assert Solution().squareIsWhite(coordinates) == expected
