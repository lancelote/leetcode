class Solution:
    def setZeroes(self, matrix: list[list[int]]) -> None:
        assert matrix
        assert matrix[0]

        rows = len(matrix)
        cols = len(matrix[0])
        first_row = matrix[0][0]

        for c in range(cols):
            if matrix[0][c] == 0:
                first_row = 0
                break

        for c in range(cols):
            for r in range(rows):
                if matrix[r][c] == 0:
                    matrix[0][c] = 0
                    break

        for r in range(1, rows):
            for c in range(cols):
                if matrix[r][c] == 0:
                    matrix[r][0] = 0
                    break

        for r in range(1, rows):
            if matrix[r][0] == 0:
                for c in range(1, cols):
                    matrix[r][c] = 0

        for c in range(cols):
            if matrix[0][c] == 0:
                for r in range(1, rows):
                    matrix[r][c] = 0

        if first_row == 0:
            for c in range(cols):
                matrix[0][c] = 0
