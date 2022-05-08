Row = list[int]
Grid = list[Row]


class Solution:
    def shiftGrid(self, grid: Grid, k: int) -> Grid:
        assert grid

        n_rows = len(grid)
        n_cols = len(grid[0])

        new_grid = [[0] * n_cols for _ in range(n_rows)]

        for i in range(n_rows):
            for j in range(n_cols):
                new_i = (i + (j + k) // n_cols) % n_rows
                new_j = (j + k) % n_cols
                new_grid[new_i][new_j] = grid[i][j]

        return new_grid
