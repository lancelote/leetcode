class Solution:
    def countNegatives(self, grid: list[list[int]]) -> int:
        n = len(grid[0])
        result = 0
        last_negative_idx = n - 1

        for line in grid:
            while last_negative_idx >= 0 and line[last_negative_idx] < 0:
                last_negative_idx -= 1

            result += n - last_negative_idx - 1

        return result
