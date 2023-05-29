import pytest

from src.is_subsequence import Solution


@pytest.mark.parametrize(
    "s,t,expected",
    (
        ("abc", "ahbgdc", True),
        ("axc", "ahbgdc", False),
    ),
)
def test_solution(s, t, expected):
    assert Solution().isSubsequence(s, t) is expected
