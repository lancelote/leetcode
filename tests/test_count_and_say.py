import pytest

from src.count_and_say import Solution


@pytest.mark.parametrize(
    "n,expected",
    [
        (1, "1"),
        (4, "1211"),
    ],
)
def test_solution(n, expected):
    assert Solution().countAndSay(n) == expected
