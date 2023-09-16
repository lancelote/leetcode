import heapq
import sys

SHIFTS = (
    (-1, 0),
    (+1, 0),
    (0, -1),
    (0, +1),
)


class Solution:
    def minimumEffortPath(self, heights: list[list[int]]) -> int:
        rows = len(heights)
        cols = len(heights[0])

        smallest = [[sys.maxsize] * cols for _ in range(rows)]
        to_visit = [(0, 0, 0)]

        while to_visit:
            r, c, path = heapq.heappop(to_visit)

            if r == rows - 1 and c == cols - 1:
                return path

            if path >= smallest[r][c]:
                continue
            else:
                smallest[r][c] = path

            for dr, dc in SHIFTS:
                nr = dr + r
                nc = dc + c

                if 0 <= nr < rows and 0 <= nc < cols:
                    new_path = abs(heights[r][c] - heights[nr][nc])
                    heapq.heappush(to_visit, (nr, nc, max(path, new_path)))

        raise ValueError("path not found")
