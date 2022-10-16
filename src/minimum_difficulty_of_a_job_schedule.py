import sys


class Solution:
    def minDifficulty(self, jobs: list[int], d: int) -> int:
        n = len(jobs)
        if n < d:
            return -1

        dp = [[sys.maxsize] * n + [0] for _ in range(d + 1)]

        for i in range(1, d + 1):
            for j in range(n - i + 1):
                max_d = 0
                for k in range(j, n - i + 1):
                    max_d = max(max_d, jobs[k])
                    dp[i][j] = min(dp[i][j], max_d + dp[i - 1][k + 1])

        return dp[-1][0]
