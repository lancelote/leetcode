import pytest

from src.guess_number_higher_or_lower import Solution


@pytest.mark.parametrize(
    "n,pick,expected",
    [
        (
            10,
            6,
            6,
        ),
        (1, 1, 1),
        (2, 1, 1),
    ],
)
def test_solution(n, pick, expected, monkeypatch):
    monkeypatch.setenv("SECRET", str(pick))
    assert Solution().guessNumber(n) == expected
