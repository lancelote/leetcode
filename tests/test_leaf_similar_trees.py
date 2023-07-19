import pytest

from src.leaf_similar_trees import Solution
from src.utils.binary_tree import list_to_tree


@pytest.mark.parametrize(
    "in_list1,in_list2,expected",
    (
        (
            [3, 5, 1, 6, 2, 9, 8, None, None, 7, 4],
            [3, 5, 1, 6, 7, 4, 2, None, None, None, None, None, None, 9, 8],
            True,
        ),
        ([1, 2, 3], [1, 3, 2], False),
    ),
)
def test_solution(in_list1, in_list2, expected):
    root1 = list_to_tree(in_list1)
    root2 = list_to_tree(in_list2)

    assert Solution().leafSimilar(root1, root2) is expected
