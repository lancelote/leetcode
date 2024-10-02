import pytest

from src.substring_with_concatenation_of_all_words import Solution


@pytest.mark.parametrize(
    "s,words,expected",
    (
        ("barfoothefoobarman", ["foo", "bar"], [0, 9]),
        ("wordgoodgoodgoodbestword", ["word", "good", "best", "word"], []),
        ("barfoofoobarthefoobarman", ["bar", "foo", "the"], [6, 9, 12]),
    ),
)
def test_solution(s, words, expected):
    assert Solution().findSubstring(s, words) == expected
