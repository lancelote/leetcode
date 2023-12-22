SHIFTS = (
    (-1, 0),
    (0, +1),
    (+1, 0),
    (0, -1),
)


class Solution:
    def maxAreaOfIsland(self, grid: list[list[int]]) -> int:
        rows = len(grid)
        cols = len(grid[0])

        max_area = 0
        seen: set[tuple[int, int]] = set()

        def dfs(r: int, c: int) -> int:
            nonlocal max_area

            if (r, c) in seen:
                return 0

            if r < 0 or r >= rows or c < 0 or c >= cols:
                return 0

            if not grid[r][c]:
                return 0

            seen.add((r, c))
            count = 1

            for dr, dc in SHIFTS:
                count += dfs(r + dr, c + dc)

            return count

        for r in range(rows):
            for c in range(cols):
                if grid[r][c] and (r, c) not in seen:
                    area = dfs(r, c)
                    max_area = max(max_area, area)

        return max_area
