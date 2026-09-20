import pytest

from src.reverse_degree_of_a_string import Solution


@pytest.mark.parametrize(
    "s,expected",
    (
        ("abc", 148),
        ("zaza", 160),
    ),
)
def test_solution(s, expected):
    assert Solution().reverseDegree(s) == expected
