import pytest

from src.odd_string_difference import Solution


@pytest.mark.parametrize(
    "words,expected",
    [
        (["adc", "wzy", "abc"], "abc"),
        (["aaa", "bob", "ccc", "ddd"], "bob"),
    ],
)
def test_solution(words, expected):
    assert Solution().oddString(words) == expected
