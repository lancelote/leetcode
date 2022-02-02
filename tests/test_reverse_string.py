import pytest

from src.reverse_string import Solution


@pytest.mark.parametrize(
    "s,expected",
    [
        (["h", "e", "l", "l", "o"], ["o", "l", "l", "e", "h"]),
        (["H", "a", "n", "n", "a", "h"], ["h", "a", "n", "n", "a", "H"]),
    ],
)
def test_solution(s, expected):
    Solution().reverseString(s)
    assert s == expected
