import pytest

from src.word_break import Solution


@pytest.mark.parametrize(
    "s,word_dict,expected",
    [
        ("leetcode", ["leet", "code"], True),
        ("applepenapple", ["apple", "pen"], True),
        ("catsandog", ["cats", "dog", "sand", "and", "cat"], False),
    ],
)
def test_solution(s, word_dict, expected):
    assert Solution().wordBreak(s, word_dict) is expected
