import pytest

from src.remove_colored_pieces_if_both_neighbors_are_the_same_color import (
    Solution,
)


@pytest.mark.parametrize(
    "colors,expected",
    (
        ("AAABABB", True),
        ("AA", False),
        ("ABBBBBBBAAA", False),
    ),
)
def test_solution(colors, expected):
    assert Solution().winnerOfGame(colors) == expected
