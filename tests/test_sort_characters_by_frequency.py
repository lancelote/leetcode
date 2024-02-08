import pytest

from src.sort_characters_by_frequency import Solution


@pytest.mark.parametrize(
    "s,expected",
    (
        ("tree", "eetr"),
        ("cccaaa", "cccaaa"),
        ("Aabb", "bbAa"),
    ),
)
def test_solution(s, expected):
    assert Solution().frequencySort(s) == expected
