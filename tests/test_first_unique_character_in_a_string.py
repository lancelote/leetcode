import pytest

from src.first_unique_character_in_a_string import Solution


@pytest.mark.parametrize(
    "s,expected",
    (
        ("leetcode", 0),
        ("loveleetcode", 2),
        ("aabb", -1),
    ),
)
def test_solution(s, expected):
    assert Solution().firstUniqChar(s) == expected
