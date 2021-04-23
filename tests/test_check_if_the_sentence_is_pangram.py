import pytest

from src.check_if_the_sentence_is_pangram import Solution


@pytest.mark.parametrize(
    "sentence,is_pangram",
    [
        ("thequickbrownfoxjumpsoverthelazydog", True),
        ("leetcode", False),
    ],
)
def test_solution(sentence, is_pangram):
    assert Solution().checkIfPangram(sentence) == is_pangram
