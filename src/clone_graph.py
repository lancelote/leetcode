from src.utils.undirected_graph import Node


class Solution:
    def cloneGraph(self, root: Node | None) -> Node | None:
        index_to_node: dict[int, Node] = {}

        def dfs(node: Node | None) -> Node | None:
            if not node:
                return None

            if node.val in index_to_node:
                return index_to_node[node.val]

            new_node = Node(node.val)
            index_to_node[new_node.val] = new_node
            neighbors: list[Node] = []

            for neighbor in node.neighbors:
                new_neighbor = dfs(neighbor)
                if new_neighbor:
                    neighbors.append(new_neighbor)

            new_node.neighbors = neighbors
            return new_node

        return dfs(root)
