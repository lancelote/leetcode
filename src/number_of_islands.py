SHIFTS = [
    (-1, 0),
    (0, +1),
    (+1, 0),
    (0, -1),
]


class Solution:
    def numIslands(self, grid: list[list[str]]) -> int:
        assert grid
        assert grid[0]

        rows = len(grid)
        cols = len(grid[0])

        visited: set[tuple[int, int]] = set()
        islands = 0

        def visit(r: int, c: int) -> None:
            if not (0 <= r < rows and 0 <= c < cols):
                return
            if grid[r][c] == "0":
                return
            if (r, c) in visited:
                return

            visited.add((r, c))
            for dr, dc in SHIFTS:
                visit(r + dr, c + dc)

        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == "1" and (r, c) not in visited:
                    islands += 1
                    visit(r, c)

        return islands
