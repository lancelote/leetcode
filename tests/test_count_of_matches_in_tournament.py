import pytest

from src.count_of_matches_in_tournament import Solution


@pytest.mark.parametrize(
    "n,expected",
    [
        (8, 7),
        (9, 8),
        (7, 6),
        (14, 13),
    ],
)
def test_solution(n, expected):
    assert Solution().numberOfMatches(n) == expected
