import pytest

from src.split_linked_list_in_parts import Solution
from src.utils.linked_list import to_linked_list
from src.utils.linked_list import to_list


@pytest.mark.parametrize(
    "in_list,k,expected_out",
    (
        ([1, 2, 3], 5, [[1], [2], [3], [], []]),
        (
            [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],
            3,
            [[1, 2, 3, 4], [5, 6, 7], [8, 9, 10]],
        ),
    ),
)
def test_solution(in_list, k, expected_out):
    head = to_linked_list(in_list)
    result = Solution().splitListToParts(head, k)
    assert [to_list(x) for x in result] == expected_out
