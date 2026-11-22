import pytest

from src.power_of_two import Solution


@pytest.mark.parametrize(
    "n,expected",
    (
        (1, True),
        (16, True),
        (3, False),
        (-16, False),
    ),
)
def test_solution(n, expected):
    assert Solution().isPowerOfTwo(n) is expected
