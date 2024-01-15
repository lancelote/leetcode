import pytest

from src.letter_combinations_of_a_phone_number import Solution


@pytest.mark.parametrize(
    "digits,result",
    (
        ("23", ["ad", "ae", "af", "bd", "be", "bf", "cd", "ce", "cf"]),
        ("", []),
        ("2", ["a", "b", "c"]),
    ),
)
def test_solution(digits, result):
    assert Solution().letterCombinations(digits) == result
