ALPHA = 1/10**5


def get_area_below(limit: float, squares: list[list[int]]) -> float:
    area = 0

    for _, y, h in squares:
        if y < limit:
            area += h * min(limit - y, h)

    return area


class Solution:
    def separateSquares(self, squares: list[list[int]]) -> float:
        max_y = 0
        total_area = 0

        for _, y, h in squares:
            total_area += h * h
            max_y = max(max_y, y + h)

        low, high = 0, max_y
        while abs(high - low) > ALPHA:
            mid = (high + low) / 2
            if get_area_below(mid, squares) >= total_area / 2:
                high = mid
            else:
                low = mid

        return high
