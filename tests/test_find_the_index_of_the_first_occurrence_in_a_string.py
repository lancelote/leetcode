import pytest

from src.find_the_index_of_the_first_occurrence_in_a_string import Solution


@pytest.mark.parametrize(
    "expected,haystack,needle",
    (
        (0, "sadbutsad", "sad"),
        (-1, "leetcode", "leeto"),
    ),
)
def test_solution(expected, haystack, needle):
    assert expected == Solution().strStr(haystack, needle)
