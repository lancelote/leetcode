SHIFTS = (
    (-1, 0),
    (0, +1),
    (+1, 0),
    (0, -1),
)


class Solution:
    def numIslands(self, grid: list[list[str]]) -> int:
        rows = len(grid)
        cols = len(grid[0])

        count = 0
        visited: set[tuple[int, int]] = set()

        def dfs(r: int, c: int) -> None:
            if (r, c) in visited:
                return

            if r < 0 or r >= rows or c < 0 or c >= cols:
                return

            if grid[r][c] == "0":
                return

            visited.add((r, c))
            for dr, dc in SHIFTS:
                dfs(r + dr, c + dc)

        for r in range(rows):
            for c in range(cols):
                if (r, c) not in visited and grid[r][c] == "1":
                    count += 1
                    dfs(r, c)

        return count
