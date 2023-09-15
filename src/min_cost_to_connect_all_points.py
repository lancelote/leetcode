import heapq
from typing import cast
from typing import TypeAlias

Point: TypeAlias = tuple[int, int]
Cost: TypeAlias = int


def get_cost(p1: Point, p2: Point) -> Cost:
    x1, y1 = p1
    x2, y2 = p2

    return abs(x1 - x2) + abs(y1 - y2)


class Solution:
    def minCostConnectPoints(self, data: list[list[int]]) -> int:
        points = cast(list[Point], [tuple(x) for x in data])
        n = len(points)

        total_cost = 0
        start_point = points[0]

        visited: set[Point] = set()
        frontier: list[tuple[Cost, Point]] = [(0, start_point)]

        while len(visited) != n:
            closest_cost, closest_point = heapq.heappop(frontier)
            if closest_point in visited:
                continue

            visited.add(closest_point)
            total_cost += closest_cost

            for point in points:
                if tuple(point) not in visited:
                    cost = get_cost(closest_point, point)
                    heapq.heappush(frontier, (cost, point))

        return total_cost
