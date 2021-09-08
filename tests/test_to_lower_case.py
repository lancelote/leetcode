import pytest

from src.to_lower_case import Solution


@pytest.mark.parametrize(
    "string,expected",
    [
        ("Hello", "hello"),
        ("here", "here"),
        ("LOVELY", "lovely"),
    ],
)
def test_solution(string, expected):
    assert Solution().toLowerCase(string) == expected
