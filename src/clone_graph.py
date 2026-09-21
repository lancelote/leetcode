from src.utils.undirected_graph import Node


class Solution:
    def cloneGraph(self, root: Node | None) -> Node | None:
        if root is None:
            return None

        old_to_new: dict[Node, Node] = {}

        def dfs(old_node: Node | None) -> None:
            if old_node is None:
                return

            if old_node in old_to_new:
                return

            new_node = Node(val=old_node.val)
            old_to_new[old_node] = new_node

            for node in old_node.neighbors:
                dfs(node)

        dfs(root)

        for old_node, new_node in old_to_new.items():
            new_node.neighbors = [
                old_to_new[node] for node in old_node.neighbors
            ]

        return old_to_new[root]
