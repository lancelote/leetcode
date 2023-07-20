import pytest

from src.put_marbles_in_bags import Solution


@pytest.mark.parametrize(
    "weights,k,expected",
    (
        ([1, 3, 5, 1], 2, 4),
        ([1, 3], 2, 0),
    ),
)
def test_solution(weights, k, expected):
    assert Solution().putMarbles(weights, k) == expected
