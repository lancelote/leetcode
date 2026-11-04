import heapq
import sys


class Solution:
    def minimumCost(
        self, n: int, highways: list[list[int]], discounts: int
    ) -> int:
        graph: list[list[tuple[int, int]]] = [[] for _ in range(n)]
        for u, v, toll in highways:
            graph[u].append((v, toll))
            graph[v].append((u, toll))

        h = [(0, 0, 0)]  # cost, city, discounts used
        dp = [[sys.maxsize] * (discounts + 1) for _ in range(n)]
        dp[0][0] = 0
        visited = [[False] * (discounts + 1) for _ in range(n)]

        while h:
            cost, city, discounts_used = heapq.heappop(h)

            if city == n - 1:
                return cost

            if visited[city][discounts_used]:
                continue
            visited[city][discounts_used] = True

            for neighbor, toll in graph[city]:
                # don't use the discount
                new_cost = cost + toll
                if new_cost < dp[neighbor][discounts_used]:
                    dp[neighbor][discounts_used] = new_cost
                    heapq.heappush(h, (new_cost, neighbor, discounts_used))

                # use the discount
                if discounts_used < discounts:
                    new_cost = cost + toll // 2
                    if new_cost < dp[neighbor][discounts_used + 1]:
                        dp[neighbor][discounts_used + 1] = new_cost
                        heapq.heappush(
                            h, (new_cost, neighbor, discounts_used + 1)
                        )

        return -1
