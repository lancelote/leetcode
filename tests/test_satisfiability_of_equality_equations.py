import pytest

from src.satisfiability_of_equality_equations import Solution


@pytest.mark.parametrize(
    "equations,expected",
    [
        (["a==b", "b!=a"], False),
        (["b==a", "a==b"], True),
    ],
)
def test_solution(equations, expected):
    assert Solution().equationsPossible(equations) is expected
