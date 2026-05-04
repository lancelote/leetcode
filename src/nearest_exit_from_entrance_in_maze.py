from collections import deque

SHIFTS = (
    (-1, 0),  # up
    (0, +1),  # left
    (+1, 0),  # down
    (0, -1),  # left
)


class Solution:
    def nearestExit(self, maze: list[list[str]], entrance: list[int]) -> int:
        n_rows = len(maze)
        n_cols = len(maze[0])

        sr, sc = entrance
        seen = {(sr, sc)}
        to_visit = deque([(sr, sc)])

        steps = 0
        while to_visit:
            for _ in range(len(to_visit)):
                r, c = to_visit.popleft()

                if (
                    r == 0 or r == n_rows - 1 or c == 0 or c == n_cols - 1
                ) and (r, c) != (sr, sc):
                    return steps

                for dr, dc in SHIFTS:
                    nr = r + dr
                    nc = c + dc

                    if (
                        (nr, nc) not in seen
                        and 0 <= nr < n_rows
                        and 0 <= nc < n_cols
                        and maze[nr][nc] == "."
                    ):
                        to_visit.append((nr, nc))
                        seen.add((nr, nc))

            steps += 1

        return -1
