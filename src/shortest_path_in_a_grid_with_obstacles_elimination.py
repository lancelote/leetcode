import sys

SHIFTS = (
    # row, col
    (-1, 0),  # top
    (0, +1),  # right
    (+1, 0),  # bottom
    (0, -1),  # left
)


class Solution:
    def shortestPath(self, grid: list[list[int]], k: int) -> int:
        assert grid
        assert grid[0]

        shortest = sys.maxsize
        rows = len(grid)
        cols = len(grid[0])

        if k >= rows + cols - 2:
            return rows + cols - 2

        seen: set[tuple[int, int]] = set()

        def dfs(r: int, c: int, path: int, k: int) -> None:
            nonlocal shortest

            if (r, c) in seen:
                return  # already visited
            seen.add((r, c))

            if r == rows - 1 and c == cols - 1:
                shortest = min(shortest, path)

            if r < 0 or r >= rows or c < 0 or c >= cols:
                seen.remove((r, c))
                return  # out of bounds

            if grid[r][c] == 1:
                if not k:
                    seen.remove((r, c))
                    return  # wall and no eliminations left
                else:
                    k -= 1  # wall but we can eliminate it

            for dr, dc in SHIFTS:
                dfs(r + dr, c + dc, path + 1, k)

            seen.remove((r, c))

        dfs(r=0, c=0, path=0, k=k)
        return shortest if shortest != sys.maxsize else -1
