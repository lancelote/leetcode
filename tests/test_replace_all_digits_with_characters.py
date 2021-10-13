import pytest

from src.replace_all_digits_with_characters import Solution


@pytest.mark.parametrize(
    "letter,index,expected",
    [
        ("a", 5, "f"),
        ("x", 0, "x"),
    ],
)
def test_shift(letter, index, expected):
    assert Solution().shift(letter, index) == expected


@pytest.mark.parametrize(
    "s,expected", [("a1c1e1", "abcdef"), ("a1b2c3d4e", "abbdcfdhe")]
)
def test_replace_digits(s, expected):
    assert Solution().replaceDigits(s) == expected
