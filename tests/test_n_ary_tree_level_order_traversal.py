from src.n_ary_tree_level_order_traversal import Node
from src.n_ary_tree_level_order_traversal import Solution


def test_1():
    root = Node(
        1,
        [
            Node(
                3,
                [
                    Node(5),
                    Node(6),
                ],
            ),
            Node(2),
            Node(4),
        ],
    )
    assert Solution().levelOrder(root) == [[1], [3, 2, 4], [5, 6]]


def test_2():
    root = Node(
        1,
        [
            Node(2),
            Node(
                3,
                [
                    Node(6),
                    Node(
                        7,
                        [
                            Node(
                                11,
                                [
                                    Node(14),
                                ],
                            ),
                        ],
                    ),
                ],
            ),
            Node(
                4,
                [
                    Node(
                        8,
                        [
                            Node(12),
                        ],
                    ),
                ],
            ),
            Node(
                5,
                [
                    Node(
                        9,
                        [
                            Node(13),
                        ],
                    ),
                    Node(10),
                ],
            ),
        ],
    )
    assert Solution().levelOrder(root) == [
        [1],
        [2, 3, 4, 5],
        [6, 7, 8, 9, 10],
        [11, 12, 13],
        [14],
    ]


def test_empty():
    assert Solution().levelOrder(None) == []


def test_zero_val():
    assert Solution().levelOrder(Node(0)) == [[0]]
