import pytest

from src.words_within_two_edits_of_dictionary import Solution


@pytest.mark.parametrize(
    "queries,dictionary,expected",
    [
        (
            ["word", "note", "ants", "wood"],
            ["wood", "joke", "moat"],
            ["word", "note", "wood"],
        ),
        (["yes"], ["not"], []),
        (
            [
                "prfturjd",
                "iarapqqk",
                "aokbrtmx",
                "yafmjorj",
                "larakqqk",
                "nliynmpm",
                "isikkcws",
                "laraeqqk",
            ],
            ["apahhijt", "larapqqk", "isukkcws", "siqqoacj", "nloynmpm"],
            ["iarapqqk", "larakqqk", "nliynmpm", "isikkcws", "laraeqqk"],
        ),
    ],
)
def test_solution(queries, dictionary, expected):
    assert Solution().twoEditWords(queries, dictionary) == expected
