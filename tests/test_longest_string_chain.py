import pytest

from src.longest_string_chain import Solution


@pytest.mark.parametrize(
    "words,expected",
    (
        (["a", "b", "ba", "bca", "bda", "bdca"], 4),
        (["xbc", "pcxbcf", "xb", "cxbc", "pcxbc"], 5),
        (["abcd", "dbqca"], 1),
    ),
)
def test_solution(words, expected):
    assert Solution().longestStrChain(words) == expected
