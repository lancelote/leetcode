import pytest

from src.odd_even_linked_list import Solution
from src.utils.linked_list import to_linked_list
from src.utils.linked_list import to_list


@pytest.mark.parametrize(
    "in_list,out_list",
    (
        ([1, 2, 3, 4, 5], [1, 3, 5, 2, 4]),
        ([2, 1, 3, 5, 6, 4, 7], [2, 3, 6, 7, 1, 5, 4]),
    ),
)
def test_solution(in_list, out_list):
    head = to_linked_list(in_list)
    result = Solution().oddEvenList(head)
    assert to_list(result) == out_list
