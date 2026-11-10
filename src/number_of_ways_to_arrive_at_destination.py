import heapq
import sys

MOD = 10**9 + 7


class Solution:
    def countPaths(self, n: int, roads: list[list[int]]) -> int:
        graph: list[list[tuple[int, int]]] = [[] for _ in range(n)]

        for u, v, time in roads:
            graph[u].append((v, time))
            graph[v].append((u, time))

        h = [(0, 0)]  # time, node
        shortest_time = [sys.maxsize] * n
        path_count = [0] * n

        shortest_time[0] = 0
        path_count[0] = 1

        while h:
            current_time, node = heapq.heappop(h)

            if current_time > shortest_time[node]:
                continue

            for neighbor, time in graph[node]:
                new_time = time + current_time

                if new_time < shortest_time[neighbor]:
                    shortest_time[neighbor] = new_time
                    path_count[neighbor] = path_count[node]
                    heapq.heappush(h, (new_time, neighbor))

                elif new_time == shortest_time[neighbor]:
                    path_count[neighbor] = (
                        path_count[neighbor] + path_count[node]
                    ) % MOD

        return path_count[n - 1]
