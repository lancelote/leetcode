class Solution:
    def rotate(self, matrix: list[list[int]]) -> None:
        assert matrix
        assert matrix[0]

        n = len(matrix)

        for r in range(n // 2):
            for c in range(r, n - r - 1):
                tmp = matrix[r][c]
                matrix[r][c] = matrix[n - c - 1][r]
                matrix[n - c - 1][r] = matrix[n - r - 1][n - c - 1]
                matrix[n - r - 1][n - c - 1] = matrix[c][n - r - 1]
                matrix[c][n - r - 1] = tmp
