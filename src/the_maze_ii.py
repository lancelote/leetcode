import heapq
from collections import defaultdict
from typing import Iterator

type Node = tuple[int, int]

SHIFTS = (
    (0, -1),  # left
    (-1, 0),  # up
    (0, 1),  # right
    (1, 0),  # down
)


def get_edges(
    node: tuple[int, int],
    maze: list[list[int]]
) -> Iterator[tuple[int, Node]]:
    rows = len(maze)
    cols = len(maze[0])

    for dr, dc in SHIFTS:
        distance = 0
        r, c = node

        while 0 <= (nr := r + dr) < rows and 0 <= (nc := c + dc) < cols and maze[nr][nc] == 0:
            r = nr
            c = nc
            distance += 1

        if node != (r, c):
            yield distance, (r, c)


class Solution:
    def shortestDistance(
        self,
        maze: list[list[int]],
        start: list[int],
        destination: list[int]
    ) -> int:
        graph: dict[Node, list[tuple[int, Node]]] = defaultdict(list)
        for r, row in enumerate(maze):
            for c, x in enumerate(row):
                node = (r, c)

                if x == 0:
                    for distance, neighbor in get_edges(node, maze):
                        graph[node].append((distance, neighbor))

        target = (destination[0], destination[1])
        h = [(0, (start[0], start[1]))]
        visited = set[Node]()

        while h:
            current_distance, node = heapq.heappop(h)

            if node == target:
                return current_distance

            if node in visited:
                continue

            visited.add(node)

            for distance, neighbor in graph[node]:
                if neighbor not in visited:
                    heapq.heappush(h, (distance + current_distance, neighbor))

        return -1
