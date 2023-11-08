class Solution:
    def isReachableAtTime(
        self, sx: int, sy: int, fx: int, fy: int, t: int
    ) -> bool:
        if sx == fx and sy == fy and t == 1:
            return False

        distance = max(abs(sx - fx), abs(sy - fy))
        return distance <= t
