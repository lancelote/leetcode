import pytest

from src.increasing_decreasing_string import Solution


@pytest.mark.parametrize(
    "s,expected",
    [
        ("aaaabbbbcccc", "abccbaabccba"),
        ("rat", "art"),
    ],
)
def test_solution(s, expected):
    assert Solution().sortString(s) == expected
