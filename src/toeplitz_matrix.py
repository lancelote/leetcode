class Solution:
    def isToeplitzMatrix(self, matrix: list[list[int]]) -> bool:
        assert matrix
        assert matrix[0]

        rows = len(matrix)
        cols = len(matrix[0])

        for c in range(-rows + 1, cols):
            row: set[int] = set()

            for r in range(rows):
                if 0 <= r + c < cols:
                    row.add(matrix[r][r + c])
                    if len(row) > 1:
                        return False

        return True
