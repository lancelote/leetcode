import pytest

from src.count_square_sum_triples import Solution


@pytest.mark.parametrize(
    "n,count",
    [
        (5, 2),
        (10, 4),
        (18, 10),
    ],
)
def test_solution(n, count):
    assert Solution().countTriples(n) == count
