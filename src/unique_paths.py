class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        cache = [[0] * n for _ in range(m)]

        def dfs(r: int, c: int) -> int:
            if r == m or c == n:
                return 0
            if r == m - 1 and c == n - 1:
                return 1
            if cache[r][c]:
                return cache[r][c]
            cache[r][c] = dfs(r + 1, c) + dfs(r, c + 1)
            return cache[r][c]

        return dfs(0, 0)
