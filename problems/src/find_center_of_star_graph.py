class Solution:
    def findCenter(self, edges: list[list[int]]) -> int:
        [[node_a, node_b], second_edge, *_] = edges
        return node_a if node_a in second_edge else node_b
