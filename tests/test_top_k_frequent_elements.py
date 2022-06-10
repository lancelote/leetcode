import pytest

from src.top_k_frequent_elements import Solution


@pytest.mark.parametrize(
    "nums,k,expected", [([1, 1, 1, 2, 2, 3], 2, [1, 2]), ([1], 1, [1])]
)
def test_solution(nums, k, expected):
    return Solution().topKFrequent(nums, k) == expected
