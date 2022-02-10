from collections import deque
from typing import Deque
from typing import Iterator
from typing import NamedTuple

Image = list[list[int]]


class Pixel(NamedTuple):
    x: int
    y: int
    value: int


SHIFTS = [
    (0, +1),
    (+1, 0),
    (0, -1),
    (-1, 0),
]


def neighbors(pixel: Pixel, image: Image) -> Iterator[Pixel]:
    for dx, dy in SHIFTS:
        new_x = pixel.x + dx
        new_y = pixel.y + dy

        valid_x = 0 <= new_x < len(image[0])
        valid_y = 0 <= new_y < len(image)

        if valid_x and valid_y:
            yield Pixel(new_x, new_y, value=image[new_y][new_x])


class Solution:
    def floodFill(self, image: Image, y: int, x: int, new_color: int) -> Image:
        assert image
        assert image[0]

        start_pixel = Pixel(x, y, value=image[y][x])
        base_color = start_pixel.value

        if new_color == base_color:
            return image

        to_paint: Deque[Pixel] = deque()
        to_paint.append(start_pixel)

        while to_paint:
            pixel = to_paint.popleft()
            image[pixel.y][pixel.x] = new_color

            for neighbor in neighbors(pixel, image):
                if neighbor.value == base_color:
                    to_paint.append(neighbor)

        return image
