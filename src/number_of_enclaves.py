SHIFTS = (
    (-1, 0),  # up
    (0, +1),  # right
    (+1, 0),  # down
    (0, -1),  # left
)


class Solution:
    def numEnclaves(self, grid: list[list[int]]) -> int:
        assert grid

        n_rows = len(grid)
        n_cols = len(grid[0])

        if n_rows < 3 or n_cols < 3:
            return 0

        # iterate outer layer
        def dfs(r: int, c: int) -> None:
            if grid[r][c] != 1:
                return

            grid[r][c] = -1

            for dr, dc in SHIFTS:
                nr = r + dr
                nc = c + dc

                if 0 <= nr < n_rows and 0 <= nc < n_cols and grid[nr][nc] == 1:
                    dfs(nr, nc)

        # top
        for i in range(n_cols):
            dfs(0, i)

        # right
        for i in range(1, n_rows):
            dfs(i, n_cols - 1)

        # down
        for i in range(n_cols - 2, -1, -1):
            dfs(n_rows - 1, i)

        # left
        for i in range(n_rows - 2, 0, -1):
            dfs(i, 0)

        # count inner
        result = 0

        for i in range(1, n_rows - 1):
            for j in range(1, n_cols - 1):
                if grid[i][j] == 1:
                    result += 1

        return result
