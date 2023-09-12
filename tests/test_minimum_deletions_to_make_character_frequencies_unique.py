import pytest

from src.minimum_deletions_to_make_character_frequencies_unique import Solution


@pytest.mark.parametrize(
    "s,expected",
    (
        ("aab", 0),
        ("aaabbbcc", 2),
        ("ceabaacb", 2),
    ),
)
def test_solution(s, expected):
    assert Solution().minDeletions(s) == expected
