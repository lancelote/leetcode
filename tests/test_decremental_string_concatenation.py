import pytest

from src.decremental_string_concatenation import Solution


@pytest.mark.parametrize(
    "words,expected",
    (
        (["aa", "ab", "bc"], 4),
        (["ab", "b"], 2),
        (["aaa", "c", "aba"], 6),
        (["ab", "bc", "db", "ed"], 6),
        (["aa", "bc", "bb"], 5),
        (
            [
                "jif",
                "abhd",
                "jif",
                "ihi",
                "acd",
                "f",
                "dihf",
                "cag",
                "bb",
                "jcg",
                "c",
                "bfhga",
                "i",
                "ahh",
                "de",
                "egje",
                "f",
                "gfeec",
                "cddg",
                "fgiad",
                "ga",
            ],
            56,
        ),
    ),
)
def test_solution(words, expected):
    assert Solution().minimizeConcatenatedLength(words) == expected
