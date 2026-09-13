import sys


class Solution:
    def minPathSum(self, grid: list[list[int]]) -> int:
        n_rows = len(grid)
        n_cols = len(grid[0])

        path_sums = [[sys.maxsize] * n_cols for _ in range(n_rows)]

        def dfs(r: int, c: int, so_far: int) -> None:
            if not (0 <= r < n_rows):
                return

            if not (0 <= c < n_cols):
                return

            so_far += grid[r][c]

            if so_far >= path_sums[r][c]:
                return

            path_sums[r][c] = so_far

            dfs(r + 1, c, so_far)
            dfs(r, c + 1, so_far)

        dfs(0, 0, 0)
        return path_sums[-1][-1]
