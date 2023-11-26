MOD = 10**9 + 7


class Solution:
    def numRollsToTarget(self, n: int, k: int, target: int) -> int:
        dp = [[0] * target for _ in range(n)]

        for i in range(min(k, target)):
            dp[0][i] = 1

        for r in range(1, n):
            for c in range(r, target):
                dp[r][c] = sum(
                    dp[r - 1][c - i] for i in range(1, k + 1) if c - i >= 0
                )

        return dp[-1][-1] % MOD
