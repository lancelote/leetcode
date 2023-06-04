import pytest

from src.max_number_of_k_sum_pairs import Solution


@pytest.mark.parametrize(
    "nums,k,expected",
    (
        ([1, 2, 3, 4], 5, 2),
        ([3, 1, 3, 4, 3], 6, 1),
        ([1, 1, 2, 2], 3, 2),
        ([3, 1, 5, 1, 1, 1, 1, 1, 2, 2, 3, 2, 2], 1, 0),
    ),
)
def test_solution(nums, k, expected):
    assert Solution().maxOperations(nums, k) == expected
