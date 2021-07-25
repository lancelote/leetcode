import pytest

from src.check_if_all_characters_have_equal_number_of_occurrences import (
    Solution,
)


@pytest.mark.parametrize(
    "s,expected",
    [
        ("abacbc", True),
        ("aaabb", False),
    ],
)
def test_solution(s, expected):
    assert Solution().areOccurrencesEqual(s) == expected
