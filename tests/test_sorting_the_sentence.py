import pytest

from src.sorting_the_sentence import Solution


@pytest.mark.parametrize(
    "sentence,expected",
    [
        ("is2 sentence4 This1 a3", "This is a sentence"),
        ("Myself2 Me1 I4 and3", "Me Myself and I"),
    ],
)
def test_solution(sentence, expected):
    assert Solution().sortSentence(sentence) == expected
