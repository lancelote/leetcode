class Solution:
    def findMinArrowShots(self, points: list[list[int]]) -> int:
        sorted_points = sorted(points)

        arrows = 1
        _, last_end = points[0]

        for start, end in sorted_points:
            if start > last_end:
                arrows += 1
                last_end = end
            else:
                last_end = min(last_end, end)

        return arrows
