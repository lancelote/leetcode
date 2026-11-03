import pytest

from src.maximum_candies_allocated_to_k_children import Solution


@pytest.mark.parametrize(
    "candies,k,expected",
    (
        ([5, 8, 6], 3, 5),
        ([2, 5], 11, 0),
    ),
)
def test_solution(candies, k, expected):
    assert Solution().maximumCandies(candies, k) == expected
