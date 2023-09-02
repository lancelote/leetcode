import pytest

from src.extra_characters_in_a_string import Solution


@pytest.mark.parametrize(
    "s,dictionary,expected",
    (
        ("leetscode", ["leet", "code", "leetcode"], 1),
        ("sayhelloworld", ["hello", "world"], 3),
    ),
)
def test_solution(s, dictionary, expected):
    assert Solution().minExtraChar(s, dictionary) == expected
