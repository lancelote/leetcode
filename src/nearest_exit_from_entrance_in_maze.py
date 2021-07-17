from collections import deque


def neighbors(position: tuple[int, int, int]) -> list[tuple[int, int, int]]:
    x, y, step = position
    return [
        (x + 1, y, step + 1),
        (x - 1, y, step + 1),
        (x, y + 1, step + 1),
        (x, y - 1, step + 1),
    ]


class Solution:
    def nearestExit(self, maze: list[list[str]], entrance: list[int]) -> int:
        assert maze

        height = len(maze) - 1
        width = len(maze[0]) - 1

        def in_maze(x: int, y: int) -> bool:
            return 0 <= x <= height and 0 <= y <= width

        def is_exit(x: int, y: int) -> bool:
            return x == 0 or y == 0 or x == height or y == width

        seen = set()
        positions: deque[tuple[int, int, int]] = deque()

        start_x, start_y = entrance

        seen.add((start_x, start_y))
        positions.append((start_x, start_y, 0))

        while positions:
            position = positions.popleft()
            for neighbor in neighbors(position):
                x, y, step = neighbor

                if (x, y) in seen or not in_maze(x, y):
                    continue

                seen.add((x, y))

                if maze[x][y] == ".":
                    if is_exit(x, y):
                        return step
                    positions.append(neighbor)

        return -1
