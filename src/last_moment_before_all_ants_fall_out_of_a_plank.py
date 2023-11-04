class Solution:
    def getLastMoment(self, n: int, left: list[int], right: list[int]) -> int:
        if not left and not right:
            return 0
        elif not left:
            return n - min(right)
        elif not right:
            return max(left)

        return max(n - min(right), max(left))
