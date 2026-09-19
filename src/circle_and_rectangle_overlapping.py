import math


def distance(x1: int, y1: int, x2: int, y2: int) -> float:
    return math.sqrt((x1 - x2) ** 2 + (y1 - y2) ** 2)


class Solution:
    def checkOverlap(
        self,
        radius: int,
        x_center: int,
        y_center: int,
        x1: int,
        y1: int,
        x2: int,
        y2: int,
    ) -> bool:
        # distances from center to corners
        # left-bottom
        if distance(x_center, y_center, x1, y1) <= radius:
            return True

        # left-top
        if distance(x_center, y_center, x1, y2) <= radius:
            return True

        # right-top
        if distance(x_center, y_center, x2, y2) <= radius:
            return True

        # right-bottom
        if distance(x_center, y_center, x2, y1) <= radius:
            return True

        # position of circle horizontal and vertical points
        # left
        if x1 <= x_center - radius <= x2 and y1 <= y_center <= y2:
            return True

        # top
        if x1 <= x_center <= x2 and y1 <= y_center + radius <= y2:
            return True

        # right
        if x1 <= x_center + radius <= x2 and y1 <= y_center <= y2:
            return True

        # bottom
        if x1 <= x_center <= x2 and y1 <= y_center - radius <= y2:
            return True

        # rectangle center is inside the circle
        if y1 < y_center < y2 and (x_center - radius) < x1 < (
            x_center + radius
        ):
            return True

        if x1 < x_center < x2 and (y_center - radius) < y1 < (
            y_center + radius
        ):
            return True

        return False
