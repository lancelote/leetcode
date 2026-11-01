import pytest

from src.reverse_words_in_a_string_ii import Solution


@pytest.mark.parametrize(
    "s,expected",
    (
        (
            [
                "t",
                "h",
                "e",
                " ",
                "s",
                "k",
                "y",
                " ",
                "i",
                "s",
                " ",
                "b",
                "l",
                "u",
                "e",
            ],
            [
                "b",
                "l",
                "u",
                "e",
                " ",
                "i",
                "s",
                " ",
                "s",
                "k",
                "y",
                " ",
                "t",
                "h",
                "e",
            ],
        ),
        (
            ["a"],
            ["a"],
        ),
    ),
)
def test_solution(s, expected):
    Solution().reverseWords(s)
    assert s == expected
