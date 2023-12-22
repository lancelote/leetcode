from collections import deque
from typing import Deque

SHIFTS = (
    (-1, 0),
    (-1, +1),
    (0, +1),
    (+1, +1),
    (+1, 0),
    (+1, -1),
    (0, -1),
    (-1, -1),
)


class Solution:
    def shortestPathBinaryMatrix(self, grid: list[list[int]]) -> int:
        rows = len(grid)
        cols = len(grid[0])

        length = 1

        visited: set[tuple[int, int]] = set()
        queue: Deque[tuple[int, int]] = deque()

        if not grid[0][0]:
            visited.add((0, 0))
            queue.append((0, 0))

        while queue:
            for _ in range(len(queue)):
                r, c = queue.popleft()

                if r == rows - 1 and c == cols - 1:
                    return length

                for dr, dc in SHIFTS:
                    nr = r + dr
                    nc = c + dc

                    if (
                        0 <= nr < rows
                        and 0 <= nc < cols
                        and not grid[nr][nc]
                        and (nr, nc) not in visited
                    ):
                        visited.add((nr, nc))
                        queue.append((nr, nc))

            length += 1

        return -1
