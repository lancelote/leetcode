import pytest

from src.count_binary_substrings import Solution


@pytest.mark.parametrize(
    "s,expected",
    (
        ("1", 0),
        ("10", 1),
        ("00110011", 6),
        ("10101", 4),
        ("00100", 2),
    ),
)
def test_solution(s, expected):
    assert Solution().countBinarySubstrings(s) == expected
