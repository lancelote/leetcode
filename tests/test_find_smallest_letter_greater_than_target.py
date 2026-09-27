import pytest

from src.find_smallest_letter_greater_than_target import Solution


@pytest.mark.parametrize(
    "letters,target,expected",
    (
        (["c", "f", "j"], "a", "c"),
        (["c", "f", "j"], "c", "f"),
        (["x", "x", "y", "y"], "z", "x"),
        (["c", "f", "j"], "j", "c"),
    ),
)
def test_solution(letters, target, expected):
    assert Solution().nextGreatestLetter(letters, target) == expected
