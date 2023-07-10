import pytest

from src.removing_stars_from_a_string import Solution


@pytest.mark.parametrize(
    "s,expected",
    (
        ("leet**cod*e", "lecoe"),
        ("erase*****", ""),
    ),
)
def test_solution(s, expected):
    assert Solution().removeStars(s) == expected
