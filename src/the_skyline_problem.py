import heapq
import sys


class Solution:
    def getSkyline(self, buildings: list[list[int]]) -> list[list[int]]:
        points = [(left, -height, right) for left, right, height in buildings]
        points += [(right, 0, 0) for _, right, _ in buildings]
        points.sort()

        result: list[list[int]] = []
        heap = [(0, sys.maxsize)]

        for left, height, right in points:
            while heap[0][1] <= left:
                heapq.heappop(heap)

            if height:
                heapq.heappush(heap, (height, right))

            if not result or result[-1][1] != -heap[0][0]:
                result.append([left, -heap[0][0]])

        return result
