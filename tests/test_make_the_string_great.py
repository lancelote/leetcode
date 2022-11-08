import pytest

from src.make_the_string_great import Solution


@pytest.mark.parametrize(
    "s,expected",
    [
        ("leEeetcode", "leetcode"),
        ("abBAcC", ""),
        ("s", "s"),
        ("", ""),
    ],
)
def test_solution(s, expected):
    assert Solution().makeGood(s) == expected
