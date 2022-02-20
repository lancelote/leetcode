import pytest

from src.permutation_in_string import Solution


@pytest.mark.parametrize(
    "s1,s2,expected",
    [
        ("ab", "eidbaooo", True),
        ("ab", "eidboaoo", False),
        ("ab", "a", False),
    ],
)
def test_solution(s1, s2, expected):
    assert Solution().checkInclusion(s1, s2) is expected
