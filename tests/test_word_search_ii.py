import pytest

from src.word_search_ii import Solution


@pytest.mark.parametrize(
    "board,words,expected_words",
    [
        (
            [
                ["o", "a", "a", "n"],
                ["e", "t", "a", "e"],
                ["i", "h", "k", "r"],
                ["i", "f", "l", "v"],
            ],
            ["oath", "pea", "eat", "rain"],
            ["eat", "oath"],
        ),
        ([["a", "b"], ["c", "d"]], ["abcb"], []),
        (
            [
                ["o", "a", "b", "n"],
                ["o", "t", "a", "e"],
                ["a", "h", "k", "r"],
                ["a", "f", "l", "v"],
            ],
            ["oa", "oaa"],
            ["oa", "oaa"],
        ),
        ([["a", "a"]], ["aaa"], []),
        (
            [
                ["o", "a", "a", "n"],
                ["e", "t", "a", "e"],
                ["i", "h", "k", "r"],
                ["i", "f", "l", "v"],
            ],
            ["oath", "pea", "eat", "rain", "hklf", "hf"],
            ["oath", "eat", "hklf", "hf"],
        ),
    ],
)
def test_solution(board, words, expected_words):
    assert set(Solution().findWords(board, words)) == set(expected_words)
