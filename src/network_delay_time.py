import heapq


class Solution:
    def networkDelayTime(self, times: list[list[int]], n: int, k: int) -> int:
        graph: list[list[tuple[int, int]]] = [[] for _ in range(n + 1)]
        for u, v, time in times:
            graph[u].append((v, time))

        h = [(0, k)]  # time, node
        visited = set[int]()

        while h:
            current_time, node = heapq.heappop(h)

            visited.add(node)

            if len(visited) == n:
                return current_time

            for neighbor, time in graph[node]:
                if neighbor not in visited:
                    heapq.heappush(h, (current_time + time, neighbor))

        return -1
