class Solution:
    @staticmethod
    def sec_between(a: list[int], b: list[int]) -> int:
        return max(abs(a[0] - b[0]), abs(a[1] - b[1]))

    def minTimeToVisitAllPoints(self, points: list[list[int]]) -> int:
        return sum(
            self.sec_between(points[i], points[i + 1])
            for i in range(0, len(points) - 1)
        )
