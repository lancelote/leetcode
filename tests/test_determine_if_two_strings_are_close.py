import pytest

from src.determine_if_two_strings_are_close import Solution


@pytest.mark.parametrize(
    "word1,word2,expected",
    (
        ("abc", "bca", True),
        ("a", "aa", False),
        ("cabbba", "abbccc", True),
        ("abbzccca", "babzzczc", True),
    ),
)
def test_solution(word1, word2, expected):
    assert Solution().closeStrings(word1, word2) is expected
