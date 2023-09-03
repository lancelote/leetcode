class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        dp = [1] * n

        for i in range(m - 2, -1, -1):
            new_dp = [0] * n
            new_dp[-1] = 1

            for j in range(n - 2, -1, -1):
                new_dp[j] = new_dp[j + 1] + dp[j]

            dp = new_dp

        return dp[0]
