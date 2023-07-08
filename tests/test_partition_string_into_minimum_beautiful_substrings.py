import pytest

from src.partition_string_into_minimum_beautiful_substrings import Solution


@pytest.mark.parametrize(
    "s,expected",
    (
        ("1011", 2),
        ("111", 3),
        ("0", -1),
        ("101101101111001", 5),
        ("10110111111011", 4),
        ("01011", -1),
    ),
)
def test_solution(s, expected):
    assert Solution().minimumBeautifulSubstrings(s) == expected
