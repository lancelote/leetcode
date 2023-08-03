class Solution:
    def tribonacci(self, n: int) -> int:
        cache = [0, 1, 1]

        if n < 3:
            return cache[n]

        for _ in range(3, n + 1):
            cache[0], cache[1], cache[2] = cache[1], cache[2], sum(cache)

        return cache[-1]
