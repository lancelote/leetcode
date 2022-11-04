import pytest

from src.longest_palindrome_by_concatenating_two_letter_words import Solution


@pytest.mark.parametrize(
    "words,expected",
    [
        (["lc", "cl", "gg"], 6),
        (["ab", "ty", "yt", "lc", "cl", "ab"], 8),
        (["cc", "ll", "xx"], 2),
        (
            [
                "dd",
                "aa",
                "bb",
                "dd",
                "aa",
                "dd",
                "bb",
                "dd",
                "aa",
                "cc",
                "bb",
                "cc",
                "dd",
                "cc",
            ],
            22,
        ),
    ],
)
def test_solution(words, expected):
    assert Solution().longestPalindrome(words) == expected
