class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        cols = len(text1)
        rows = len(text2)

        dp = [[0] * cols for _ in range(rows)]

        def dfs(r: int, c: int) -> int:
            if r >= rows or c >= cols:
                return 0

            if dp[r][c]:
                return dp[r][c]

            if text1[c] == text2[r]:
                result = 1 + dfs(r + 1, c + 1)
            else:
                result = max(dfs(r + 1, c), dfs(r, c + 1))

            dp[r][c] = result
            return result

        dfs(0, 0)
        return dp[0][0]
