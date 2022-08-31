SHIFTS = [
    (-1, 0),
    (0, +1),
    (+1, 0),
    (0, -1),
]


class Solution:
    def pacificAtlantic(self, heights: list[list[int]]) -> list[list[int]]:
        assert heights
        assert heights[0]

        rows = len(heights)
        cols = len(heights[0])

        pacific: set[tuple[int, int]] = set()
        atlantic: set[tuple[int, int]] = set()

        def dfs(
            r: int, c: int, ocean: set[tuple[int, int]], prev: int
        ) -> None:
            if (r, c) in ocean:
                return
            if r < 0 or r == rows or c < 0 or c == cols:
                return
            if heights[r][c] < prev:
                return
            ocean.add((r, c))
            for dr, dc in SHIFTS:
                dfs(r + dr, c + dc, ocean, heights[r][c])

        # first and last row
        for c in range(cols):
            dfs(0, c, pacific, heights[0][c])
            dfs(rows - 1, c, atlantic, heights[rows - 1][c])

        # first and last column
        for r in range(rows):
            dfs(r, 0, pacific, heights[r][0])
            dfs(r, cols - 1, atlantic, heights[r][cols - 1])

        # conversion to list is required by the task
        return [[r, c] for r, c in pacific & atlantic]
