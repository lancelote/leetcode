import pytest

from src.determine_if_string_halves_are_alike import Solution


@pytest.mark.parametrize(
    "text,expected",
    [
        ("book", True),
        ("textbook", False),
        ("MerryChristmas", False),
        ("AbCdEfGh", True),
    ],
)
def test_solution(text, expected):
    assert Solution().halvesAreAlike(text) == expected
