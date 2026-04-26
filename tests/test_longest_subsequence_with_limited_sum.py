import pytest

from src.longest_subsequence_with_limited_sum import Solution


@pytest.mark.parametrize(
    "nums,queries,expected",
    (
        ([4, 5, 2, 1], [3, 10, 21], [2, 3, 4]),
        ([2, 3, 4, 5], [1], [0]),
    ),
)
def test_solution(nums, queries, expected):
    assert Solution().answerQueries(nums, queries) == expected
