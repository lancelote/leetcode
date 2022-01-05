import pytest

from src.maximum_number_of_words_found_in_sentences import Solution


@pytest.mark.parametrize(
    "sentences,max_len",
    [
        (
            [
                "alice and bob love leetcode",
                "i think so too",
                "this is great thanks very much",
            ],
            6,
        ),
        (["please wait", "continue to fight", "continue to win"], 3),
    ],
)
def test_solution(sentences, max_len):
    assert Solution().mostWordsFound(sentences) == max_len
