import pytest

from src.merge_two_sorted_lists import Solution
from src.utils.linked_list import assert_linked_list
from src.utils.linked_list import to_linked_list


@pytest.mark.parametrize(
    "l1,l2,expected",
    [
        ([1, 2, 4], [1, 3, 4], [1, 1, 2, 3, 4, 4]),
        ([], [], []),
        ([], [0], [0]),
    ],
)
def test_solution(l1, l2, expected):
    result = Solution().mergeTwoLists(to_linked_list(l1), to_linked_list(l2))
    assert_linked_list(result, to_linked_list(expected))
