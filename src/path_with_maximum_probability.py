import heapq


class Solution:
    def maxProbability(
        self,
        n: int,
        edges: list[list[int]],
        succ_prob: list[float],
        start_node: int,
        end_node: int,
    ) -> float:
        graph: list[list[tuple[int, float]]] = [[] for _ in range(n)]

        for i, [u, v] in enumerate(edges):
            w = succ_prob[i]

            graph[u].append((v, w))
            graph[v].append((u, w))

        h = [(1.0, start_node)]  # probability, node

        probabilities: list[float] = [0] * n

        while h:
            current_probability, node = heapq.heappop_max(h)

            if node == end_node:
                return current_probability

            if current_probability < probabilities[node]:
                continue

            for neighbor, probability in graph[node]:
                new_probability = probability * current_probability

                if new_probability > probabilities[neighbor]:
                    probabilities[neighbor] = new_probability
                    heapq.heappush_max(h, (new_probability, neighbor))

        return 0
