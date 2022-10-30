from collections import deque

SHIFTS = (
    # row, col
    (+1, 0),  # bottom
    (-1, 0),  # top
    (0, +1),  # right
    (0, -1),  # left
)


class Solution:
    def shortestPath(self, grid: list[list[int]], k: int) -> int:
        assert grid
        assert grid[0]

        rows = len(grid)
        cols = len(grid[0])

        if k >= rows + cols - 2:
            return rows + cols - 2

        dq = deque([(0, 0, k, 0)])  # row, col, k, path
        seen: set[tuple[int, int, int]] = set()

        while dq:
            r, c, k, path = dq.popleft()
            if (r, c) == (rows - 1, cols - 1):
                return path

            for dr, dc in SHIFTS:
                nr = r + dr
                nc = c + dc

                if 0 <= nr < rows and 0 <= nc < cols and k >= grid[nr][nc]:
                    if (nr, nc, k) not in seen:
                        seen.add((nr, nc, k))
                        dq.append((nr, nc, k - grid[nr][nc], path + 1))

        return -1
