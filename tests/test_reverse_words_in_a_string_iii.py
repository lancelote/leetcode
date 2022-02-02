import pytest

from src.reverse_words_in_a_string_iii import Solution


@pytest.mark.parametrize(
    "s,expected",
    [
        ("Let's take LeetCode contest", "s'teL ekat edoCteeL tsetnoc"),
        ("God Ding", "doG gniD"),
    ],
)
def test_solution(s, expected):
    assert Solution().reverseWords(s) == expected
