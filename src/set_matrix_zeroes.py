def set_row_none(matrix: list[list[int | None]], r: int) -> None:
    for c in range(len(matrix[0])):
        if matrix[r][c] != 0:
            matrix[r][c] = None


def set_col_none(matrix: list[list[int | None]], c: int) -> None:
    for row in matrix:
        if row[c] != 0:
            row[c] = None


class Solution:
    def setZeroes(self, matrix: list[list[int | None]]) -> None:
        for r, row in enumerate(matrix):
            for c, item in enumerate(row):
                if item == 0:
                    set_row_none(matrix, r)
                    set_col_none(matrix, c)

        for r, row in enumerate(matrix):
            for c, item in enumerate(row):
                if item is None:
                    matrix[r][c] = 0
