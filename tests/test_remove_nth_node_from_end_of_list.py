import pytest

from src.remove_nth_node_from_end_of_list import Solution
from src.utils.linked_list import is_equal
from src.utils.linked_list import to_linked_list


@pytest.mark.parametrize(
    "head_array,n,expected_array",
    [
        ([1, 2, 3, 4, 5], 2, [1, 2, 3, 5]),
        ([1], 1, []),
        ([1, 2], 1, [1]),
    ],
)
def test_solution(head_array, n, expected_array):
    head = to_linked_list(head_array)
    expected = to_linked_list(expected_array)

    assert is_equal(Solution().removeNthFromEnd(head, n), expected)
