import pytest

from src.check_if_string_is_a_prefix_of_array import Solution


@pytest.mark.parametrize(
    "s,words,expected",
    (
        ("iloveleetcode", ["i", "love", "leetcode", "apples"], True),
        ("iloveleetcode", ["apples", "i", "love", "leetcode"], False),
    ),
)
def test_solution(s, words, expected):
    assert Solution().isPrefixString(s, words) == expected
