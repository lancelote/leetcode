import pytest

from src.push_dominoes import Solution


@pytest.mark.parametrize(
    "dominoes,expected",
    [
        ("RR.L", "RR.L"),
        (".L.R...LR..L..", "LL.RR.LLRRLL.."),
    ],
)
def test_solution(dominoes, expected):
    assert Solution().pushDominoes(dominoes) == expected
