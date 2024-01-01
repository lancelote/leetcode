from collections import deque


SHIFTS = (
    (0, -1),
    (+1, 0),
    (0, +1),
    (-1, 0),
)


class Solution:
    def nearestExit(self, maze: list[list[str]], entrance: list[int]) -> int:
        rows = len(maze)
        cols = len(maze[0])

        visited: set[tuple[int, int]] = set()

        start = (entrance[0], entrance[1])
        d: deque[tuple[int, int]] = deque()

        visited.add(start)
        d.append(start)

        path = 0

        while d:
            for _ in range(len(d)):
                r, c = d.popleft()

                if (r == 0 or r == rows - 1 or c == 0 or c == cols - 1) and (
                    r,
                    c,
                ) != start:
                    return path

                for dr, dc in SHIFTS:
                    nr = r + dr
                    nc = c + dc

                    if (
                        0 <= nr < rows
                        and 0 <= nc < cols
                        and maze[nr][nc] == "."
                        and (nr, nc) not in visited
                    ):
                        d.append((nr, nc))
                        visited.add((nr, nc))

            path += 1

        return -1
