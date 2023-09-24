import pytest

from src.champagne_tower import Solution


@pytest.mark.parametrize(
    "poured,query_row,query_glass,expected",
    (
        (1, 1, 1, 0),
        (2, 1, 1, 0.5),
        (100000009, 33, 17, 1),
        (25, 6, 1, 0.18750),
    ),
)
def test_solution(poured, query_row, query_glass, expected):
    assert (
        Solution().champagneTower(poured, query_row, query_glass) == expected
    )
