import heapq

SHIFTS = (
    (0, -1),  # left
    (-1, 0),  # up
    (0, 1),  # right
    (1, 0),  # down
)


class Solution:
    def maximumMinimumPath(self, grid: list[list[int]]) -> int:
        rows = len(grid)
        cols = len(grid[0])

        target = (rows - 1, cols - 1)

        h = [(grid[0][0], (0, 0))]  # cost, node
        visited = [[False] * cols for _ in range(rows)]

        min_path_value = grid[0][0]
        visited[0][0] = True

        while h:
            cost, (r, c) = heapq.heappop_max(h)

            min_path_value = min(min_path_value, cost)

            if (r, c) == target:
                break

            for dr, dc in SHIFTS:
                nr = r + dr
                nc = c + dc

                if 0 <= nr < rows and 0 <= nc < cols and not visited[nr][nc]:
                    heapq.heappush_max(h, (grid[nr][nc], (nr, nc)))
                    visited[nr][nc] = True

        return min_path_value
