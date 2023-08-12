class Solution:
    def uniquePathsWithObstacles(self, grid: list[list[int]]) -> int:
        if grid[-1][-1]:
            return 0

        rows = len(grid)
        cols = len(grid[0])

        dp = [0] * cols
        dp[-1] = 1

        for r in range(rows - 1, -1, -1):
            new_dp = [0] * cols

            for c in range(cols - 1, -1, -1):
                if grid[r][c]:
                    new_dp[c] = 0
                    continue

                if r < rows:
                    new_dp[c] += dp[c]
                if c < (cols - 1):
                    new_dp[c] += new_dp[c + 1]

            dp = new_dp
        return dp[0]
