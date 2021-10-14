import pytest

from src.remove_outermost_parentheses import Solution


@pytest.mark.parametrize(
    "text,expected",
    [
        ("(()())(())", "()()()"),
        ("(()())(())(()(()))", "()()()()(())"),
        ("()()", ""),
    ],
)
def test_solution(text, expected):
    assert Solution().removeOuterParentheses(text) == expected
