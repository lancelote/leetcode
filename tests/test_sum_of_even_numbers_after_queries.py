import pytest

from src.sum_of_even_numbers_after_queries import Solution


@pytest.mark.parametrize(
    "nums,queries,expected_sum",
    [
        ([1, 2, 3, 4], [[1, 0], [-3, 1], [-4, 0], [2, 3]], [8, 6, 2, 4]),
        ([1], [[4, 0]], [0]),
    ],
)
def test_solution(nums, queries, expected_sum):
    assert Solution().sumEvenAfterQueries(nums, queries) == expected_sum
