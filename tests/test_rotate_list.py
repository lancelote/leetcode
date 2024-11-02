import pytest

from src.rotate_list import Solution
from src.utils.linked_list import to_linked_list
from src.utils.linked_list import to_list


@pytest.mark.parametrize(
    "in_list,k,expected_out_list",
    (
        ([1, 2, 3, 4, 5], 2, [4, 5, 1, 2, 3]),
        ([0, 1, 2], 4, [2, 0, 1]),
        ([], 0, []),
        ([], 1, []),
        ([1], 1, [1]),
        ([1, 2], 2, [1, 2]),
        ([1], 99, [1]),
    ),
)
def test_solution(in_list, k, expected_out_list):
    head = to_linked_list(in_list)
    out_head = Solution().rotateRight(head, k)
    out_list = to_list(out_head)
    assert out_list == expected_out_list
