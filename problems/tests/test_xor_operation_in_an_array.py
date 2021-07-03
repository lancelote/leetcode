import pytest
from src.xor_operation_in_an_array import Solution


@pytest.mark.parametrize(
    "n,start,expected",
    [
        (5, 0, 8),
        (4, 3, 8),
        (1, 7, 7),
        (10, 5, 2),
    ],
)
def test_solution(n, start, expected):
    assert Solution().xorOperation(n, start) == expected
