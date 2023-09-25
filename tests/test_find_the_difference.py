import pytest

from src.find_the_difference import Solution


@pytest.mark.parametrize(
    "s,t,expected",
    (
        ("abcd", "abcde", "e"),
        ("", "y", "y"),
    ),
)
def test_solution(s, t, expected):
    assert Solution().findTheDifference(s, t) == expected
