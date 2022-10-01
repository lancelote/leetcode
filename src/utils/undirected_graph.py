from __future__ import annotations


class Node:
    def __init__(self, val: int = 0, neighbors: list[Node] = None) -> None:
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []

    def __repr__(self) -> str:
        return f"Node({self.val})"


def list_to_node(adj_list: list[list[int]]) -> Node | None:
    if not adj_list:
        return None

    node_map: dict[int, Node] = {}

    for i in range(len(adj_list)):
        if i + 1 in node_map:
            node = node_map[i + 1]
        else:
            node = Node(val=i + 1)
            node_map[i + 1] = node

        for child_i in adj_list[i]:
            if child_i in node_map:
                child = node_map[child_i]
            else:
                child = Node(val=child_i)
                node_map[child_i] = child
            node.neighbors.append(child)

    return node_map[1]


def node_to_list(root: Node | None) -> list[list[int]]:
    result: list[list[int]] = []
    node_map: dict[int, Node] = {}

    def visit(node: Node | None) -> None:
        if not node:
            return

        if node.val in node_map:
            return

        node_map[node.val] = node

        for child in node.neighbors:
            visit(child)

    visit(root)

    for i in range(len(node_map)):
        result.append([child.val for child in node_map[i + 1].neighbors])

    return result
