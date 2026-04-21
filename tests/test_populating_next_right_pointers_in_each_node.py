from src.populating_next_right_pointers_in_each_node import Node
from src.populating_next_right_pointers_in_each_node import Solution


def test_example():
    n6 = Node(6)
    n7 = Node(7)
    n3 = Node(3, left=n6, right=n7)
    n4 = Node(4)
    n5 = Node(5)
    n2 = Node(2, left=n4, right=n5)
    n1 = Node(1, left=n2, right=n3)

    Solution().connect(n1)

    assert n1.next is None
    assert n2.next is n3 and n3.next is None
    assert n4.next is n5 and n5.next is n6 and n6.next is n7 and n7.next is None


def test_empty():
    assert Solution().connect(None) is None
