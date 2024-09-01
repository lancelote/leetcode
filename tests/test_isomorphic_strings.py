import pytest

from src.isomorphic_strings import Solution


@pytest.mark.parametrize(
    "expected,s,t",
    (
        (True, "egg", "add"),
        (False, "foo", "bar"),
        (True, "paper", "title"),
        (False, "badc", "baba"),
    ),
)
def test_solution(expected, s, t):
    assert expected is Solution().isIsomorphic(s, t)
