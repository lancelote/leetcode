import pytest

from src.check_if_two_string_arrays_are_equivalent import Solution


@pytest.mark.parametrize(
    "word1,word2,equal",
    [
        (["ab", "c"], ["a", "bc"], True),
        (["a", "cb"], ["ab", "c"], False),
        (["abc", "d", "defg"], ["abcddefg"], True),
        (["a", "b"], ["a", "b", "c"], False),
        (["abc", "d", "defg"], ["abcddef"], False),
    ],
)
def test_solution(word1, word2, equal):
    assert Solution().arrayStringsAreEqual(word1, word2) == equal
