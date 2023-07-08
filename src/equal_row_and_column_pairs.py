from collections import defaultdict


class Solution:
    def equalPairs(self, grid: list[list[int]]) -> int:
        count = 0
        rows: dict[tuple[int, ...], int] = defaultdict(int)
        for row in grid:
            rows[tuple(row)] += 1

        for i in range(len(grid)):
            col = []
            for j in range(len(grid)):
                col.append(grid[j][i])
            count += rows[tuple(col)]

        return count
