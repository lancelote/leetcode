import pytest

from src.find_a_corresponding_node_of_a_binary_tree_in_a_clone_of_that_tree import (  # noqa
    Solution,
)
from src.utils.binary_tree import find_node
from src.utils.binary_tree import list_to_tree


@pytest.mark.parametrize(
    "in_list,x",
    (
        ([7, 4, 3, None, None, 6, 19], 3),
        ([7], 7),
    ),
)
def test_solution(in_list, x):
    tree = list_to_tree(in_list)
    target = find_node(tree, x)

    assert target is not None
    assert Solution().getTargetCopy(tree, tree, target) is target
