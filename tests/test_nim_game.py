import pytest

from src.nim_game import Solution


@pytest.mark.parametrize(
    "n,expected",
    (
        (4, False),
        (1, True),
        (2, True),
    ),
)
def test_solution(n, expected):
    assert Solution().canWinNim(n) is expected
