import pytest

from src.k_th_symbol_in_grammar import Solution


@pytest.mark.parametrize(
    "n,k,expected",
    (
        (1, 1, 0),
        (2, 1, 0),
        (2, 2, 1),
        (3, 3, 1),
    ),
)
def test_solution(n, k, expected):
    assert Solution().kthGrammar(n, k) == expected
