import sys


class Solution:
    def findTheCity(
        self, n: int, edges: list[list[int]], distance_threshold: int
    ) -> int:
        distance_matrix = [[sys.maxsize] * n for _ in range(n)]

        for i in range(n):
            distance_matrix[i][i] = 0

        for u, v, w in edges:
            distance_matrix[u][v] = w
            distance_matrix[v][u] = w

        self.floyd(n, distance_matrix)

        return self.get_fewest_neighbors_city(
            n, distance_matrix, distance_threshold
        )

    def floyd(self, n: int, distance_matrix: list[list[int]]) -> None:
        for k in range(n):
            for i in range(n):
                for j in range(n):
                    distance_matrix[i][j] = min(
                        distance_matrix[i][j],
                        distance_matrix[i][k] + distance_matrix[k][j],
                    )

    def get_fewest_neighbors_city(
        self,
        n: int,
        distance_matrix: list[list[int]],
        distance_threshold: int,
    ):
        fewest_neighbors_city = 0
        fewest_neighbors_count = sys.maxsize

        for i in range(n):
            neighbors_count = 0

            for j in range(n):
                if i == j:
                    continue

                if distance_matrix[i][j] <= distance_threshold:
                    neighbors_count += 1

            if neighbors_count <= fewest_neighbors_count:
                fewest_neighbors_count = neighbors_count
                fewest_neighbors_city = i

        return fewest_neighbors_city
