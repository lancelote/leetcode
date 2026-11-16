import heapq
import sys
from functools import lru_cache

MOD = 10**9 + 7


def dijkstra(
    n: int, distances: list[int], graph: list[list[tuple[int, int]]]
) -> None:
    distances[n] = 0
    h = [(0, n)]

    while h:
        uw, u = heapq.heappop(h)

        if uw > distances[u]:
            continue

        for v, vw in graph[u]:
            nw = vw + uw

            if nw < distances[v]:
                distances[v] = nw
                heapq.heappush(h, (nw, v))


class Solution:
    def countRestrictedPaths(self, n: int, edges: list[list[int]]) -> int:
        graph: list[list[tuple[int, int]]] = [[] for _ in range(n + 1)]
        for u, v, w in edges:
            graph[u].append((v, w))
            graph[v].append((u, w))

        distances = [sys.maxsize] * (n + 1)
        dijkstra(n, distances, graph)

        @lru_cache(None)
        def dfs(node: int) -> int:
            if node == n:
                return 1

            result = 0

            for neighbor, _ in graph[node]:
                if distances[node] > distances[neighbor]:
                    result = (result + dfs(neighbor)) % MOD

            return result

        return dfs(1)
