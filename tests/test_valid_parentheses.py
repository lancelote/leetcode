import pytest

from src.valid_parentheses import Solution


@pytest.mark.parametrize(
    "text,expected",
    [
        ("()", True),
        ("()[]{}", True),
        ("(]", False),
        ("([)]", False),
        ("{[]}", True),
        ("[", False),
        ("]", False),
    ],
)
def test_solution(text, expected):
    assert Solution().isValid(text) == expected
