Matrix = list[list[int]]


def is_diagonal(i: int, j: int, matrix: Matrix) -> bool:
    return i == j or i + j == len(matrix) - 1


class Solution:
    def diagonalSum(self, matrix: Matrix) -> int:
        total = 0

        for i, row in enumerate(matrix):
            for j, element in enumerate(row):
                if is_diagonal(i, j, matrix):
                    total += element

        return total
