def get_abs_sum(matrix: list[list[int]]) -> int:
    total = 0

    for row in matrix:
        for x in row:
            total += abs(x)

    return total


def get_min_abs_el(matrix: list[list[int]]) -> int:
    result = abs(matrix[0][0])

    for row in matrix:
        for x in row:
            abs_x = abs(x)
            result = min(result, abs_x)

    return result


class Solution:
    def maxMatrixSum(self, matrix: list[list[int]]) -> int:
        abs_sum = get_abs_sum(matrix)
        min_abs_el = get_min_abs_el(matrix)

        count_neg = 0

        for row in matrix:
            for x in row:
                if x == 0:
                    return abs_sum
                elif x < 0:
                    count_neg += 1

        if count_neg % 2 == 0:
            return abs_sum
        else:
            return abs_sum - 2 * min_abs_el
