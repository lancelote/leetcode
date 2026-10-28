import pytest

from src.one_edit_distance import Solution


@pytest.mark.parametrize(
    "s,t,expected",
    (
        ("ab", "acb", True),
        ("", "", False),
    ),
)
def test_solution(s, t, expected):
    assert Solution().isOneEditDistance(s, t) is expected
