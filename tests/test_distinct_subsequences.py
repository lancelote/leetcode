import pytest

from src.distinct_subsequences import Solution


@pytest.mark.parametrize(
    "s,t,expected",
    (
        ("rabbbit", "rabbit", 3),
        ("babgbag", "bag", 5),
    ),
)
def test_solution(s, t, expected):
    assert Solution().numDistinct(s, t) == expected
