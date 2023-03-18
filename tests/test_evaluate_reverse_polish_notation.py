import pytest

from src.evaluate_reverse_polish_notation import Solution


@pytest.mark.parametrize(
    "tokens,expected",
    [
        (["2", "1", "+", "3", "*"], 9),
        (["4", "13", "5", "/", "+"], 6),
        (
            [
                "10",
                "6",
                "9",
                "3",
                "+",
                "-11",
                "*",
                "/",
                "*",
                "17",
                "+",
                "5",
                "+",
            ],
            22,
        ),
    ],
)
def test_solution(tokens, expected):
    assert Solution().evalRPN(tokens) == expected
