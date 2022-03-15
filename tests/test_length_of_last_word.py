import pytest

from src.length_of_last_word import Solution


@pytest.mark.parametrize(
    "s,expected",
    [
        ("Hello World", 5),
        ("   fly me   to   the moon  ", 4),
        ("luffy is still joyboy", 6),
        ("Today is a nice day", 3),
        ("a", 1),
    ],
)
def test_solution(s, expected):
    assert Solution().lengthOfLastWord(s) == expected
