import pytest

from src.calculate_digit_sum_of_a_string import Solution


@pytest.mark.parametrize(
    "s,k,expected",
    (
        ("11111222223", 3, "135"),
        ("00000000", 3, "000"),
    ),
)
def test_solution(s, k, expected):
    assert Solution().digitSum(s, k) == expected
