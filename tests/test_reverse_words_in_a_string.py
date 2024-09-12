import pytest

from src.reverse_words_in_a_string import Solution


@pytest.mark.parametrize(
    "s,expected",
    [
        ("the sky is blue", "blue is sky the"),
        ("  hello world  ", "world hello"),
        ("a good   example", "example good a"),
        ("EPY2giL", "EPY2giL"),
    ],
)
def test_solution(s, expected):
    assert Solution().reverseWords(s) == expected
