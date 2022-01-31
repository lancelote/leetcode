import pytest

from src.implement_strstr import Solution


@pytest.mark.parametrize(
    "haystack,needle,expected",
    [
        ("hello", "ll", 2),
        ("aaaaa", "bba", -1),
        ("", "", 0),
    ],
)
def test_solution(haystack, needle, expected):
    assert Solution().strStr(haystack, needle) == expected
