class Solution:
    def findMinArrowShots(self, points: list[list[int]]) -> int:
        assert points

        points = sorted(points)

        n = len(points)
        arrows = 1
        _, end = points[0]

        for i in range(1, n):
            next_start, next_end = points[i]

            if next_start > end:
                arrows += 1
                end = next_end
            elif next_end < end:
                end = next_end

        return arrows
