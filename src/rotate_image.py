from typing import TypeAlias

Matrix: TypeAlias = list[list[int]]


class Solution:
    def transpose(self, matrix: Matrix) -> None:
        for c in range(len(matrix[0])):
            for r in range(c, len(matrix)):
                tmp = matrix[r][c]
                matrix[r][c] = matrix[c][r]
                matrix[c][r] = tmp

    def reverse(self, matrix: Matrix) -> None:
        for r in range(len(matrix)):
            for c in range(len(matrix[0]) // 2):
                tmp = matrix[r][c]
                matrix[r][c] = matrix[r][-c - 1]
                matrix[r][-c - 1] = tmp

    def rotate(self, matrix: Matrix) -> None:
        assert matrix
        assert matrix[0]

        self.transpose(matrix)
        self.reverse(matrix)
