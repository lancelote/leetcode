class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        dp = [0] * (n + 1)
        dp[-2] = 1

        for i in range(m - 1, -1, -1):
            new_dp = [0] * (n + 1)

            for j in range(n - 1, -1, -1):
                new_dp[j] = new_dp[j + 1] + dp[j]

            dp = new_dp

        return dp[0]
