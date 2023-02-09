class Solution:
    def oddCells(self, m: int, n: int, indices: list[list[int]]) -> int:
        matrix = [[0 for _ in range(n)] for _ in range(m)]

        for row_i, col_j in indices:
            for j in range(n):
                matrix[row_i][j] += 1
            for i in range(m):
                matrix[i][col_j] += 1

        odd_count = 0

        for row in matrix:
            for elem in row:
                if elem % 2 != 0:
                    odd_count += 1

        return odd_count
