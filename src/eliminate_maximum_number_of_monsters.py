import heapq
import math


class Solution:
    def eliminateMaximum(self, dist: list[int], speed: list[int]) -> int:
        heap: list[int] = []

        for d, s in zip(dist, speed):
            heapq.heappush(heap, math.ceil(d / s))

        step = 1
        heapq.heappop(heap)
        count = 1

        while heap:
            monster = heapq.heappop(heap)

            if monster <= step:
                return count
            else:
                count += 1

            step += 1

        return count
