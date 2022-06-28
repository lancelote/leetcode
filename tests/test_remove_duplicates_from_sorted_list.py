import pytest

from src.remove_duplicates_from_sorted_list import ListNode
from src.remove_duplicates_from_sorted_list import Solution


def from_list_to_node(data: list[int], i: int = 0) -> ListNode | None:
    if i == len(data):
        return None
    else:
        return ListNode(val=data[i], next=from_list_to_node(data, i + 1))


def from_node_to_list(node: ListNode | None) -> list[int]:
    result = []
    while node is not None:
        result.append(node.val)
        node = node.next
    return result


def test_from_list_to_node():
    lst = [1, 2, 3]
    node = from_list_to_node(lst)

    assert node.val == 1
    assert node.next.val == 2
    assert node.next.next.val == 3
    assert node.next.next.next is None


def test_from_node_to_list():
    lst_original = [1, 2, 3]
    node = from_list_to_node(lst_original)
    lst_result = from_node_to_list(node)

    assert lst_result == lst_original


@pytest.mark.parametrize(
    "head_lst,result_lst",
    [
        ([1, 1, 2], [1, 2]),
        ([1, 1, 2, 3, 3], [1, 2, 3]),
    ],
)
def test_solution(head_lst, result_lst):
    head_node = from_list_to_node(head_lst)
    result_node = Solution().deleteDuplicates(head_node)
    assert from_node_to_list(result_node) == result_lst
