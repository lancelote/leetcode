from typing import Iterator

type Node = tuple[int, int]

SHIFTS = (
    (0, -1),  # left
    (-1, 0),  # up
    (0, 1),  # right
    (1, 0),  # down
)


def iter_neighbors(node: Node, maze: list[list[int]]) -> Iterator[Node]:
    rows = len(maze)
    cols = len(maze[0])

    for dr, dc in SHIFTS:
        r, c = node

        while (
            0 <= (nr := r + dr) < rows
            and 0 <= (nc := c + dc) < cols
            and maze[nr][nc] == 0
        ):
            r = nr
            c = nc

        yield r, c


class Solution:
    def hasPath(
        self, maze: list[list[int]], start: list[int], destination: list[int]
    ) -> bool:
        target = (destination[0], destination[1])
        to_visit = [(start[0], start[1])]
        visited = set[Node]()

        while to_visit:
            node = to_visit.pop()

            if node == target:
                return True

            if node in visited:
                continue

            visited.add(node)

            for neighbor in iter_neighbors(node, maze):
                if neighbor not in visited:
                    to_visit.append(neighbor)

        return False
