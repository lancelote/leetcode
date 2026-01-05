import pytest

from src.copy_list_with_random_pointer import Node
from src.copy_list_with_random_pointer import Solution


def to_list(in_data: list[list[int | None]]) -> Node | None:
    dummy = Node(-1)
    current = dummy

    # construct the list without random
    for val, _ in in_data:
        assert val is not None

        node = Node(val)
        current.next = node
        current = current.next

    # build the node map
    int_to_node: dict[int, Node] = {}

    i = 0
    current = dummy.next

    while current:
        int_to_node[i] = current

        i += 1
        current = current.next

    # fill the random data
    i = 0
    current = dummy.next

    while current:
        _, random = in_data[i]

        if random is None:
            current.random = None
        else:
            current.random = int_to_node.get(random, None)

        i += 1
        current = current.next

    return dummy.next


def to_data(out_list: Node) -> list[list[int | None]]:
    # build the node map
    node_to_int: dict[Node, int] = {}

    i = 0
    current = out_list

    while current:
        node_to_int[current] = i

        i += 1
        current = current.next

    # construct out data with random
    out_data: list[list[int | None]] = []

    current = out_list
    while current:
        if current.random is None:
            right = None
        else:
            right = node_to_int.get(current.random, None)

        out_data.append([current.val, right])
        current = current.next

    return out_data


@pytest.mark.parametrize(
    "in_data,out_data",
    [
        (
            [[7, None], [13, 0], [11, 4], [10, 2], [1, 0]],
            [[7, None], [13, 0], [11, 4], [10, 2], [1, 0]],
        ),
        ([[1, 1], [2, 1]], [[1, 1], [2, 1]]),
        ([[3, None], [3, 0], [3, None]], [[3, None], [3, 0], [3, None]]),
    ],
)
def test_1(in_data, out_data):
    in_list = to_list(in_data)
    out_list = Solution().copyRandomList(in_list)

    assert out_list is not None
    assert to_data(out_list) == out_data
