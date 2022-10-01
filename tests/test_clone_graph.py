import pytest

from src.clone_graph import Solution
from src.utils.undirected_graph import list_to_node
from src.utils.undirected_graph import node_to_list


@pytest.mark.parametrize(
    "in_list,out_list",
    [
        ([[2, 4], [1, 3], [2, 4], [1, 3]], [[2, 4], [1, 3], [2, 4], [1, 3]]),
        ([[]], [[]]),
        ([], []),
    ],
)
def test_solution(in_list, out_list):
    root = list_to_node(in_list)
    result = Solution().cloneGraph(root)
    assert node_to_list(result) == out_list
