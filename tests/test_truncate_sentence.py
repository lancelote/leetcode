import pytest

from src.truncate_sentence import Solution


@pytest.mark.parametrize(
    "s,k,expected",
    [
        ("Hello how are you Contestant", 4, "Hello how are you"),
        ("What is the solution to this problem", 4, "What is the solution"),
        ("chopper is not a tanuki", 5, "chopper is not a tanuki"),
    ],
)
def test_solution(s, k, expected):
    assert Solution().truncateSentence(s, k) == expected
