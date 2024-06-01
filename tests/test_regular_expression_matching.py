import pytest

from src.regular_expression_matching import Solution


@pytest.mark.parametrize(
    "s,p,expected",
    (
        ("aa", "a", False),
        ("aa", "a*", True),
        ("ab", ".*", True),
        ("a", "a*b*", True),
        ("aabcbcbcaccbcaabc", ".*a*aa*.*b*.c*.*a*", True),
    ),
)
def test_solution(s, p, expected):
    assert Solution().isMatch(s, p) is expected
