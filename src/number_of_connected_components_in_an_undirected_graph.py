class Solution:
    def countConnected(self, n: int, edges: list[list[int]]) -> int:
        parent = [i for i in range(n)]
        rank = [1] * n

        def find_root(node: int) -> int:
            while node != parent[node]:
                node = parent[node]
            return node

        def union_nodes(node1: int, node2: int) -> int:
            parent1 = find_root(node1)
            parent2 = find_root(node2)

            if parent1 == parent2:
                return 0

            if rank[parent1] < rank[parent2]:
                parent[parent1] = parent2
                rank[parent2] += rank[parent1]
            else:
                parent[parent2] = parent1
                rank[parent1] += rank[parent2]

            return 1

        result = n
        for node1, node2 in edges:
            result -= union_nodes(node1, node2)

        return result
