import pytest

from src.dota2_senate import Solution


@pytest.mark.parametrize(
    "senate,expected",
    (
        ("RD", "Radiant"),
        ("RDD", "Dire"),
        ("DDRRR", "Dire"),
    ),
)
def test_solution(senate, expected):
    assert Solution().predictPartyVictory(senate) == expected
