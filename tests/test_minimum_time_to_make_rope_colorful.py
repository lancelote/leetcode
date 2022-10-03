import pytest

from src.minimum_time_to_make_rope_colorful import Solution


@pytest.mark.parametrize(
    "colors,needed_time,expected",
    [
        ("abaac", [1, 2, 3, 4, 5], 3),
        ("abc", [1, 2, 3], 0),
        ("aabaa", [1, 2, 3, 4, 1], 2),
        ("bbbaaa", [4, 9, 3, 8, 8, 9], 23),
    ],
)
def test_solution(colors, needed_time, expected):
    assert Solution().minCost(colors, needed_time) == expected
