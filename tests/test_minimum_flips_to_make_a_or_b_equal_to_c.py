import pytest

from src.minimum_flips_to_make_a_or_b_equal_to_c import Solution


@pytest.mark.parametrize(
    "a,b,c,expected",
    (
        (2, 6, 5, 3),
        (4, 2, 7, 1),
        (1, 2, 3, 0),
    ),
)
def test_solution(a, b, c, expected):
    assert Solution().minFlips(a, b, c) == expected
