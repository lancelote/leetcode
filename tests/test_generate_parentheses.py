import pytest

from src.generate_parentheses import Solution


@pytest.mark.parametrize(
    "n,expected",
    [
        (3, ["((()))", "(()())", "(())()", "()(())", "()()()"]),
        (1, ["()"]),
    ],
)
def test_solution(n, expected):
    assert Solution().generateParenthesis(n) == expected
