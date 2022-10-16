class Solution:
    def uniquePaths(self, rows: int, cols: int) -> int:
        dp = [[0] * cols for _ in range(rows)]
        dp[-1][-1] = 1

        def dfs(r: int, c: int) -> int:
            if r >= rows or c >= cols:
                return 0

            if dp[r][c] != 0:
                return dp[r][c]

            result = dfs(r + 1, c) + dfs(r, c + 1)
            dp[r][c] = result
            return result

        dfs(0, 0)
        return dp[0][0]
