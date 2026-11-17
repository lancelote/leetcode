SHIFTS = (
    (0, -1),  # left
    (-1, 0),  # up
    (0, +1),  # right
    (+1, 0),  # down
)


class Solution:
    def mark_as_visited(
        self, start: tuple[int, int], grid: list[list[str]]
    ) -> None:
        n_rows = len(grid)
        n_cols = len(grid[0])

        to_visit = [start]

        while to_visit:
            r, c = to_visit.pop()
            grid[r][c] = "0"

            for dr, dc in SHIFTS:
                nr = r + dr
                nc = c + dc

                if (
                    0 <= nr < n_rows
                    and 0 <= nc < n_cols
                    and grid[nr][nc] == "1"
                ):
                    to_visit.append((nr, nc))

    def numIslands(self, grid: list[list[str]]) -> int:
        num_of_islands = 0

        for r, row in enumerate(grid):
            for c, item in enumerate(row):
                if item == "1":
                    num_of_islands += 1
                    self.mark_as_visited((r, c), grid)

        return num_of_islands
