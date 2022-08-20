import pytest

from src.shifting_letters_ii import Solution


@pytest.mark.parametrize(
    "s,shifts,expected_s",
    [
        ("abc", [[0, 1, 0], [1, 2, 1], [0, 2, 1]], "ace"),
        ("dztz", [[0, 0, 0], [1, 1, 1]], "catz"),
    ],
)
def test_solution(s, shifts, expected_s):
    assert Solution().shiftingLetters(s, shifts) == expected_s
