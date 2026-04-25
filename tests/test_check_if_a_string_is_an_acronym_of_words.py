import pytest

from src.check_if_a_string_is_an_acronym_of_words import Solution


@pytest.mark.parametrize(
    "words,s,expected",
    (
        (["alice", "bob", "charlie"], "abc", True),
        (["an", "apple"], "a", False),
        (["never", "gonna", "give", "up", "on", "you"], "ngguoy", True),
    ),
)
def test_solution(words, s, expected):
    assert Solution().isAcronym(words, s) == expected
