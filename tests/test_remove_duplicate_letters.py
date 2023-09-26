import pytest

from src.remove_duplicate_letters import Solution


@pytest.mark.parametrize(
    "s,expected",
    (
        ("bcabc", "abc"),
        ("cbacdcbc", "acdb"),
        ("abacb", "abc"),
    ),
)
def test_solution(s, expected):
    assert Solution().removeDuplicateLetters(s) == expected
