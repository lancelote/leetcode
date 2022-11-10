import pytest

from src.remove_all_adjacent_duplicates_in_string import Solution


@pytest.mark.parametrize(
    "s,expected",
    [
        ("abbaca", "ca"),
        ("azxxzy", "ay"),
    ],
)
def test_solution(s, expected):
    assert Solution().removeDuplicates(s) == expected
