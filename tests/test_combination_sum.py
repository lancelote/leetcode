import pytest

from src.combination_sum import Solution


@pytest.mark.parametrize(
    "candidates,target,result",
    [
        ([2, 3, 6, 7], 7, [[2, 2, 3], [7]]),
        ([2, 3, 5], 8, [[2, 2, 2, 2], [2, 3, 3], [3, 5]]),
        ([2], 1, []),
        ([7], 7, [[7]]),
    ],
)
def test_solution(candidates, target, result):
    assert Solution().combinationSum(candidates, target) == result
