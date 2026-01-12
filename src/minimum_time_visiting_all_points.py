class Solution:
    def minTimeToVisitAllPoints(self, points: list[list[int]]) -> int:
        distance = 0

        for i in range(len(points) - 1):
            x1, y1 = points[i]
            x2, y2 = points[i + 1]

            dx = max(x1, x2) - min(x1, x2)
            dy = max(y1, y2) - min(y1, y2)

            distance += max(dx, dy)

        return distance
