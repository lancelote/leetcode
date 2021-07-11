import math


class Solution:
    def countTriples(self, n: int) -> int:
        count = 0
        for x in range(1, n + 1):
            for y in range(x + 1, n + 1):
                z = math.sqrt(x * x + y * y)
                if z > n:
                    break
                elif z % 1 == 0:
                    count += 2
        return count
