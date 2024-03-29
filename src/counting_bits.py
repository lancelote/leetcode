class Solution:
    def countBits(self, n: int) -> list[int]:
        result = [0] * (n + 1)

        for x in range(1, n + 1):
            result[x] = 1 + result[x & (x - 1)]

        return result
