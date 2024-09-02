import pytest

from src.word_pattern import Solution


@pytest.mark.parametrize(
    "expected,pattern,s",
    (
        (True, "abba", "dog cat cat dog"),
        (False, "abba", "dog cat cat fish"),
        (False, "aaaa", "dog cat cat dog"),
        (False, "aaa", "aa aa aa aa"),
    ),
)
def test_solution(expected, pattern, s):
    assert expected is Solution().wordPattern(pattern, s)
