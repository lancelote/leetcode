from typing import TypeAlias

Matrix: TypeAlias = list[list[int]]


def transpose(matrix: Matrix) -> None:
    rows = len(matrix)
    cols = len(matrix[0])

    for r in range(rows - 1):
        for c in range(r + 1, cols):
            matrix[r][c], matrix[c][r] = matrix[c][r], matrix[r][c]


def reflect(matrix: Matrix) -> None:
    cols = len(matrix[0])

    for r, row in enumerate(matrix):
        for c in range(cols // 2):
            new_c = cols - c - 1
            matrix[r][c], matrix[r][new_c] = matrix[r][new_c], matrix[r][c]


class Solution:
    def rotate(self, matrix: Matrix) -> None:
        transpose(matrix)
        reflect(matrix)
