from itertools import chain


class Solution:
    def diagonalSort(self, matrix: list[list[int]]) -> list[list[int]]:
        assert matrix
        assert matrix[0]

        n_rows = len(matrix)
        n_cols = len(matrix[0])

        diagonals = []

        for c in range(-n_rows + 1, n_cols):
            diagonal = []
            for r in range(n_rows):
                if 0 <= c + r < n_cols:
                    diagonal.append(matrix[r][c + r])
            diagonals.append(diagonal)

        for diagonal in diagonals:
            diagonal.sort()

        diagonal_items = chain(*diagonals)
        new_matrix = [[0] * n_cols for _ in range(n_rows)]

        for c in range(-n_rows + 1, n_cols):
            for r in range(n_rows):
                if 0 <= c + r < n_cols:
                    new_matrix[r][c + r] = next(diagonal_items)

        return new_matrix
