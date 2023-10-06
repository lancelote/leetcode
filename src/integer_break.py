class Solution:
    def integerBreak(self, n: int) -> int:
        dp = [1] * (n + 1)

        for x in range(1, n):
            for i in range(x):
                new_val = dp[i] * (x - i)
                dp[x] = max(dp[x], new_val)

        return max(dp[i] * (n - i) for i in range(1, n))
