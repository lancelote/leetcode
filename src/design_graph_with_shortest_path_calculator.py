import heapq
import sys
from collections import defaultdict


class Graph:
    def __init__(self, n: int, edges: list[list[int]]) -> None:
        self.n = n
        self.costs: dict[tuple[int, int], int] = {}
        self.conns: dict[int, list[int]] = defaultdict(list)

        for a, b, cost in edges:
            self.costs[(a, b)] = cost
            self.conns[a].append(b)

    def addEdge(self, edge: list[int]) -> None:
        a, b, cost = edge
        self.costs[(a, b)] = cost
        self.conns[a].append(b)

    def shortestPath(self, node1: int, node2: int) -> int:
        heap = [(0, node1)]
        cost_for_node = [sys.maxsize] * self.n
        cost_for_node[node1] = 0

        while heap:
            cost_for_far, a = heapq.heappop(heap)

            if a == node2:
                return cost_for_far

            if cost_for_far > cost_for_node[a]:
                continue

            for b in self.conns[a]:
                new_cost = cost_for_far + self.costs[(a, b)]

                if new_cost < cost_for_node[b]:
                    cost_for_node[b] = new_cost
                    heapq.heappush(heap, (new_cost, b))

        return -1
