import heapq
import math


def get_distance(point: list[int]) -> float:
    x, y = point
    return math.sqrt(x * x + y * y)


class Solution:
    def kClosest(self, points: list[list[int]], k: int) -> list[list[int]]:
        heap: list[tuple[float, int, int]] = []

        for point in points:
            d = get_distance(point)
            x, y = point
            heapq.heappush(heap, (-d, x, y))

            if len(heap) > k:
                heapq.heappop(heap)

        return [[x, y] for _, x, y in heap]
