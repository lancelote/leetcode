import pytest

from src.longest_unequal_adjacent_groups_subsequence_i import Solution


@pytest.mark.parametrize(
    "n,words,groups,expected",
    (
        (3, ["e", "a", "b"], [0, 0, 1], ["e", "b"]),
        (4, ["a", "b", "c", "d"], [1, 0, 1, 1], ["a", "b", "c"]),
    ),
)
def test_solution(n, words, groups, expected):
    assert (
        Solution().getWordsInLongestSubsequence(n, words, groups) == expected
    )
