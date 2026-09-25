import pytest

from src.remove_linked_list_elements import Solution
from src.utils.linked_list import to_linked_list
from src.utils.linked_list import is_equal


@pytest.mark.parametrize(
    "in_list,val,out_list",
    (
        ([1, 2, 6, 3, 4, 5, 6], 6, [1, 2, 3, 4, 5]),
        ([], 1, []),
        ([7, 7, 7, 7], 7, []),
    ),
)
def test_solution(in_list, val, out_list):
    head = to_linked_list(in_list)
    expected = to_linked_list(out_list)
    assert is_equal(Solution().removeElements(head, val), expected)
