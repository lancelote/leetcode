import pytest

from src.erect_the_fence import Solution


@pytest.mark.parametrize(
    "trees,expected",
    [
        (
            [[1, 1], [2, 2], [2, 0], [2, 4], [3, 3], [4, 2]],
            [[1, 1], [2, 0], [3, 3], [2, 4], [4, 2]],
        ),
        ([[1, 2], [2, 2], [4, 2]], [[4, 2], [2, 2], [1, 2]]),
    ],
)
def test_solution(trees, expected):
    set_expected = {(x, y) for x, y in expected}
    set_actual = {(x, y) for x, y in Solution().outerTrees(trees)}
    assert set_expected == set_actual
