from collections.abc import Iterator
from typing import Tuple

Grid = list[list[int]]
Layer = list[int]
Layers = list[Layer]
Coordinates = Tuple[int, int]


def layer_coordinates(
    layer_id: int, width: int, height: int
) -> Iterator[Coordinates]:
    x = layer_id
    y = layer_id

    for x in range(layer_id, width - layer_id):
        yield x, y

    for y in range(layer_id + 1, height - layer_id):
        yield x, y

    for x in range(width - layer_id - 2, layer_id - 1, -1):
        yield x, y

    for y in range(height - layer_id - 2, layer_id, -1):
        yield x, y


def layers_from(grid: Grid) -> Iterator[Layer]:
    grid_width = len(grid[0])
    grid_height = len(grid)
    total_layers = min(grid_width, grid_height) // 2

    for layer_id in range(total_layers):
        layer = [
            grid[y][x]
            for x, y in layer_coordinates(layer_id, grid_width, grid_height)
        ]
        yield layer


def rotate(layer: Layer, by: int) -> Iterator[int]:
    shift = by % len(layer)

    for i in range(shift, len(layer)):
        yield layer[i]

    for i in range(shift):
        yield layer[i]


class Solution:
    def rotateGrid(self, grid: Grid, k: int) -> Grid:
        grid_width = len(grid[0])
        grid_height = len(grid)

        for layer_id, layer in enumerate(layers_from(grid)):
            for (x, y), item in zip(
                layer_coordinates(layer_id, grid_width, grid_height),
                rotate(layer, by=k),
            ):
                grid[y][x] = item
        return grid
