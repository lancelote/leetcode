class Solution:
    def uniquePathsWithObstacles(self, grid: list[list[int]]) -> int:
        assert grid
        assert grid[0]

        rows = len(grid)
        cols = len(grid[0])

        row = [0] * cols
        row[-1] = 1

        for r in range(rows - 1, -1, -1):
            for c in range(cols - 1, -1, -1):
                if grid[r][c]:
                    row[c] = 0
                else:
                    row[c] += row[c + 1] if c < cols - 1 else 0

        return row[0]
