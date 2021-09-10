import math


class Solution:
    def maxMatrixSum(self, matrix: list[list[int]]) -> int:
        total_absolute = 0
        negative_count = 0
        smallest_abs = math.inf

        for row in matrix:
            for num in row:
                total_absolute += abs(num)
                smallest_abs = min(abs(num), smallest_abs)

                if num < 0:
                    negative_count += 1

        if negative_count % 2 == 0:
            return int(total_absolute)
        else:
            return int(total_absolute - 2 * smallest_abs)
