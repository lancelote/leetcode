import pytest

from src.reverse_prefix_of_word import Solution


@pytest.mark.parametrize(
    "word,ch,expected",
    [
        ("abcdefd", "d", "dcbaefd"),
        ("xyxzxe", "z", "zxyxxe"),
        ("abcd", "z", "abcd"),
        ("abcd", "d", "dcba"),
    ],
)
def test_solution(word, ch, expected):
    assert Solution().reversePrefix(word, ch) == expected
