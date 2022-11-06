import pytest

from src.orderly_queue import Solution


@pytest.mark.parametrize(
    "s,k,expected",
    [
        ("cba", 1, "acb"),
        ("baaca", 3, "aaabc"),
    ],
)
def test_solution(s, k, expected):
    assert Solution().orderlyQueue(s, k) == expected
