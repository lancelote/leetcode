from functools import cache

MOD = 10**9 + 7


class Solution:
    def numOfArrays(self, n: int, m: int, k: int) -> int:
        @cache
        def dp(i: int, max_so_far: int, remain: int) -> int:
            if remain < 0:
                return 0
            if i == n:
                return 1 if remain == 0 else 0

            # don't pick a new maximum
            res = (max_so_far * dp(i + 1, max_so_far, remain)) % MOD

            # pick a new maximum
            for x in range(max_so_far + 1, m + 1):
                res = (res + dp(i + 1, x, remain - 1)) % MOD

            return res

        return dp(0, 0, k)
