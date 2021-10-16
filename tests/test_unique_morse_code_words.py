import pytest

from src.unique_morse_code_words import Solution


@pytest.mark.parametrize(
    "word,expected",
    [
        ("gin", "--...-."),
        ("msg", "--...--."),
    ],
)
def test_to_morse(word, expected):
    assert Solution().to_morse(word) == expected


@pytest.mark.parametrize(
    "words,expected",
    [
        (["gin", "zen", "gig", "msg"], 2),
        (["a"], 1),
    ],
)
def test_solution(words, expected):
    assert Solution().uniqueMorseRepresentations(words) == expected
