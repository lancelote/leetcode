import pytest

from src.greatest_common_divisor_of_strings import Solution


@pytest.mark.parametrize(
    "str1,str2,expected",
    [
        ("ABCABC", "ABC", "ABC"),
        ("ABABAB", "ABAB", "AB"),
        ("LEET", "CODE", ""),
        ("ABCABD", "ABC", ""),
    ],
)
def test_solution(str1, str2, expected):
    assert Solution().gcdOfStrings(str1, str2) == expected
