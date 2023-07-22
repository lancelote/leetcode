import pytest

from src.sort_vowels_in_a_string import Solution


@pytest.mark.parametrize(
    "s,expected",
    (
        ("lEetcOde", "lEOtcede"),
        ("lYmpH", "lYmpH"),
    ),
)
def test_solution(s, expected):
    assert Solution().sortVowels(s) == expected
