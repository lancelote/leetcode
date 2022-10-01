from src.utils.undirected_graph import list_to_node
from src.utils.undirected_graph import Node
from src.utils.undirected_graph import node_to_list


def test_from_adj_list():
    adj_list = [[2, 4], [1, 3], [2, 4], [1, 3]]

    node1 = list_to_node(adj_list)
    node2, node4 = node1.neighbors
    _, node3 = node2.neighbors

    assert node1.val == 1
    assert node1.neighbors[0].val == 2
    assert node1.neighbors[1].val == 4

    assert node2.val == 2
    assert node2.neighbors[0].val == 1
    assert node2.neighbors[1].val == 3

    assert node3.val == 3
    assert node3.neighbors[0].val == 2
    assert node3.neighbors[1].val == 4

    assert node4.val == 4
    assert node4.neighbors[0].val == 1
    assert node4.neighbors[1].val == 3


def test_node_to_list():
    node1 = Node(1)
    node2 = Node(2)
    node3 = Node(3)
    node4 = Node(4)

    node1.neighbors = [node2, node4]
    node2.neighbors = [node1, node3]
    node3.neighbors = [node2, node4]
    node4.neighbors = [node1, node3]

    assert node_to_list(node1) == [[2, 4], [1, 3], [2, 4], [1, 3]]


def test_none_to_list():
    assert node_to_list(None) == []


def test_lone_node_to_list():
    assert node_to_list(Node(1)) == [[]]
