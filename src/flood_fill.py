from collections import deque
from typing import Deque

Image = list[list[int]]


SHIFTS = [
    (+1, 0),
    (0, +1),
    (-1, 0),
    (0, -1),
]


class Solution:
    def floodFill(
        self, image: Image, row: int, col: int, new_color: int
    ) -> Image:
        assert image
        assert image[0]

        rows = len(image)
        cols = len(image[0])
        start_pixel = (row, col)
        base_color = image[row][col]

        if new_color == base_color:
            return image

        to_paint: Deque[tuple[int, int]] = deque()
        to_paint.append(start_pixel)

        while to_paint:
            row, col = to_paint.popleft()
            valid_row = 0 <= row < rows
            valid_col = 0 <= col < cols

            if not (valid_row and valid_col) or image[row][col] != base_color:
                continue

            image[row][col] = new_color

            for d_row, d_col in SHIFTS:
                to_paint.append((row + d_row, col + d_col))

        return image
