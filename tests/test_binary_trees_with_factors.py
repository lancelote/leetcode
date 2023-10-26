import pytest

from src.binary_trees_with_factors import Solution


@pytest.mark.parametrize(
    "arr,expected",
    (
        ([2, 4], 3),
        ([2, 4, 5, 10], 7),
        ([15, 13, 22, 7, 11], 5),
    ),
)
def test_solution(arr, expected):
    assert Solution().numFactoredBinaryTrees(arr) == expected
