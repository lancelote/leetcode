import pytest

from src.word_search import Solution


@pytest.mark.parametrize(
    "board,word,expected",
    [
        (
            [["A", "B", "C", "E"], ["S", "F", "C", "S"], ["A", "D", "E", "E"]],
            "ABCCED",
            True,
        ),
        (
            [["A", "B", "C", "E"], ["S", "F", "C", "S"], ["A", "D", "E", "E"]],
            "SEE",
            True,
        ),
        (
            [["A", "B", "C", "E"], ["S", "F", "C", "S"], ["A", "D", "E", "E"]],
            "ABCB",
            False,
        ),
        ([["A"]], "A", True),
        ([["B"]], "A", False),
        ([["A", "B"], ["A", "B"]], "ABC", False),
        ([["C", "A", "A"], ["A", "A", "A"], ["B", "C", "D"]], "AAB", True),
        (
            [["a", "a", "a", "a"], ["a", "a", "a", "a"], ["a", "a", "a", "a"]],
            "aaaaaaaaaaaaa",
            False,
        ),
        ([["a", "a"], ["a", "a"]], "aaaaa", False),
    ],
)
def test_solution(board, word, expected):
    assert Solution().exist(board, word) == expected
