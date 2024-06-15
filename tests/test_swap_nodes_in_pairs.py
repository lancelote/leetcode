import pytest

from src.swap_nodes_in_pairs import Solution
from src.utils.linked_list import to_linked_list
from src.utils.linked_list import to_list


@pytest.mark.parametrize(
    "in_list,out_list",
    (
        ([1, 2, 3, 4], [2, 1, 4, 3]),
        ([], []),
        ([1], [1]),
    ),
)
def test_solution(in_list, out_list):
    head = to_linked_list(in_list)
    assert to_list(Solution().swapPairs(head)) == out_list
