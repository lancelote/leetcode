class Solution:
    def longestString(self, x: int, y: int, z: int) -> int:
        s = min(x, y) * 2

        if x != y:
            s += 1

        s += z

        return s * 2
