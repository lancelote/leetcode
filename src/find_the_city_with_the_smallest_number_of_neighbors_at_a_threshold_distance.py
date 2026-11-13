import heapq
import sys


class Solution:
    def dijkstra(
        self,
        city: int,
        graph: list[list[tuple[int, int]]],
        shortest_path: list[int],
        distance_threshold: int,
    ):
        shortest_path[city] = 0
        heap = [
            (0, city),
        ]

        while heap:
            current_distance, current_city = heapq.heappop(heap)

            if current_distance > shortest_path[current_city]:
                continue

            for neighbor, distance in graph[current_city]:
                new_distance = distance + current_distance

                if new_distance > distance_threshold:
                    continue

                if new_distance < shortest_path[neighbor]:
                    shortest_path[neighbor] = new_distance
                    heapq.heappush(heap, (new_distance, neighbor))

    def get_fewest_neighbors_city(
        self,
        n: int,
        shortest_path: list[list[int]],
        distance_threshold: int,
    ):
        best_city = -1
        fewest_neighbors_count = n

        for i in range(n):
            neighbors_count = 0

            for j in range(n):
                if i != j and shortest_path[i][j] <= distance_threshold:
                    neighbors_count += 1

            if neighbors_count <= fewest_neighbors_count:
                fewest_neighbors_count = neighbors_count
                best_city = i

        return best_city

    def findTheCity(
        self,
        n: int,
        edges: list[list[int]],
        distance_threshold: int,
    ) -> int:
        graph: list[list[tuple[int, int]]] = [[] for _ in range(n)]
        for u, v, w in edges:
            graph[u].append((v, w))
            graph[v].append((u, w))

        shortest_path = [[sys.maxsize] * n for _ in range(n)]

        for i in range(n):
            self.dijkstra(i, graph, shortest_path[i], distance_threshold)

        return self.get_fewest_neighbors_city(
            n, shortest_path, distance_threshold
        )
