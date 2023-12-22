from collections import deque
from typing import Deque

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

        fresh = 0
        minutes = 0
        seen: set[tuple[int, int]] = set()
        queue: Deque[tuple[int, int]] = deque()

        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 2:
                    seen.add((r, c))
                    queue.append((r, c))
                elif grid[r][c] == 1:
                    fresh += 1

        while queue:
            if not fresh:
                return minutes

            for _ in range(len(queue)):
                r, c = queue.popleft()

                for dr, dc in SHIFTS:
                    nr = r + dr
                    nc = c + dc

                    if (
                        0 <= nr < rows
                        and 0 <= nc < cols
                        and grid[nr][nc] == 1
                        and (nr, nc) not in seen
                    ):
                        seen.add((nr, nc))
                        queue.append((nr, nc))
                        fresh -= 1

            minutes += 1

        return -1 if fresh else 0
