import pytest

from src.middle_of_the_linked_list import ListNode
from src.middle_of_the_linked_list import OptNode
from src.middle_of_the_linked_list import Solution


def to_linked_list(array: list[int], i: int = 0) -> OptNode:
    if i == len(array):
        return None
    return ListNode(val=array[i], next=to_linked_list(array, i + 1))


def to_array(head: OptNode) -> list[int]:
    result = []

    while head is not None:
        result.append(head.val)
        head = head.next

    return result


def test_to_linked_list():
    head = to_linked_list([1, 2])

    assert isinstance(head, ListNode)
    assert head.val == 1

    assert isinstance(head.next, ListNode)
    assert head.next.val == 2

    assert head.next.next is None


def test_to_array():
    head = ListNode(1, ListNode(2, ListNode(3, None)))
    assert to_array(head) == [1, 2, 3]


@pytest.mark.parametrize(
    "input_array,expected_array",
    [
        ([1, 2, 3, 4, 5], [3, 4, 5]),
        ([1, 2, 3, 4, 5, 6], [4, 5, 6]),
    ],
)
def test_solution(input_array, expected_array):
    head = to_linked_list(input_array)
    middle_node = Solution().middleNode(head)
    result_array = to_array(middle_node)
    assert result_array == expected_array
