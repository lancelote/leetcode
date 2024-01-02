from collections import deque

SHIFTS = (
    (-1, 0),
    (0, +1),
    (+1, 0),
    (0, -1),
)


class Solution:
    def orangesRotting(self, grid: list[list[int]]) -> int:
        rows = len(grid)
        cols = len(grid[0])

        visited: set[tuple[int, int]] = set()
        d: deque[tuple[int, int]] = deque()

        minutes = 0
        fresh = 0

        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 1:
                    fresh += 1
                elif grid[r][c] == 2:
                    d.append((r, c))

        while d and fresh:
            minutes += 1

            for _ in range(len(d)):
                (r, c) = d.popleft()

                for dr, dc in SHIFTS:
                    nr = r + dr
                    nc = c + dc

                    if nr < 0 or nr >= rows or nc < 0 or nc >= cols:
                        continue

                    if (nr, nc) not in visited and grid[nr][nc] == 1:
                        visited.add((nr, nc))
                        d.append((nr, nc))
                        fresh -= 1

                        if not fresh:
                            return minutes

        return -1 if fresh else minutes
