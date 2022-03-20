import pytest

from src.add_binary import Solution


@pytest.mark.parametrize(
    "a,b,expected_sum",
    [
        ("11", "1", "100"),
        ("1010", "1011", "10101"),
        ("0", "0", "0"),
    ],
)
def test_solution(a, b, expected_sum):
    assert Solution().addBinary(a, b) == expected_sum
