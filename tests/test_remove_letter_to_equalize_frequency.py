import pytest

from src.remove_letter_to_equalize_frequency import Solution


@pytest.mark.parametrize(
    "word,expected",
    [
        ("abcc", True),
        ("aazz", False),
        ("bac", True),
        ("ddaccb", False),
        ("aaabb", True),
        ("abb", True),
        ("aabbcc", False),
        ("aaabbbcccdddd", True),
        ("abbcc", True),
        ("abbbccc", True),
        ("aabbbccc", False),
        ("aaabbcc", True),
        ("abcaa", False),
        ("abcdd", True),
    ],
)
def test_solution(word, expected):
    assert Solution().equalFrequency(word) is expected
