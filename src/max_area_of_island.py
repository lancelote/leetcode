from collections import deque
from collections.abc import Iterator
from typing import Deque

Grid = list[list[int]]
Position = tuple[int, int]


SHIFTS = [
    (0, +1),
    (+1, 0),
    (0, -1),
    (-1, 0),
]


def neighbors(position: Position, grid) -> Iterator[Position]:
    assert grid
    assert grid[0]

    x, y = position

    for dx, dy in SHIFTS:
        new_x = x + dx
        new_y = y + dy

        valid_x = 0 <= new_x < len(grid[0])
        valid_y = 0 <= new_y < len(grid)

        if valid_x and valid_y:
            yield new_x, new_y


def get_area(x: int, y: int, grid: Grid, seen: set[Position]) -> int:
    area = 0
    to_see: Deque[Position] = deque()
    to_see.append((x, y))

    def value_of(position: Position) -> int:
        position_x, position_y = position
        return grid[position_y][position_x]

    while to_see:
        current = to_see.popleft()

        if value_of(current) != 1:
            continue

        if current not in seen:
            seen.add(current)
        else:
            continue

        area += 1

        for neighbor in neighbors(current, grid):
            if neighbor not in seen and value_of(neighbor) == 1:
                to_see.append(neighbor)

    return area


class Solution:
    def maxAreaOfIsland(self, grid: Grid) -> int:
        maximum_area = 0
        seen: set[Position] = set()

        for y, row in enumerate(grid):
            for x, cell in enumerate(row):
                if cell == 1 and (x, y) not in seen:
                    area = get_area(x, y, grid, seen)
                    maximum_area = max(maximum_area, area)

        return maximum_area
