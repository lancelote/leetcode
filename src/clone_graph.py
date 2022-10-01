from src.utils.undirected_graph import Node


class Solution:
    def cloneGraph(self, root: Node | None) -> Node | None:
        node_map: dict[int, Node] = {}

        def clone(node: Node | None) -> Node | None:
            if not node:
                return None

            if node.val in node_map:
                return node_map[node.val]

            new_node = Node(val=node.val)
            node_map[node.val] = new_node
            new_node.neighbors = [clone(child) for child in node.neighbors]
            return new_node

        return clone(root)
