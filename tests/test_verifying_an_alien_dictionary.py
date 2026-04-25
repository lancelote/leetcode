import pytest

from src.verifying_an_alien_dictionary import Solution


@pytest.mark.parametrize(
    "words,order,expected",
    (
        (["hello", "leetcode"], "hlabcdefgijkmnopqrstuvwxyz", True),
        (["word", "world", "row"], "worldabcefghijkmnpqstuvxyz", False),
        (["apple", "app"], "abcdefghijklmnopqrstuvwxyz", False),
    ),
)
def test_solution(words, order, expected):
    assert Solution().isAlienSorted(words, order) is expected
