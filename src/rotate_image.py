class Solution:
    def reflect(self, matrix: list[list[int]]) -> None:
        n = len(matrix[0])

        for row in matrix:
            for col_idx in range(n // 2):
                left_idx = col_idx
                right_idx = n - col_idx - 1

                row[left_idx], row[right_idx] = row[right_idx], row[left_idx]

    def transpose(self, matrix: list[list[int]]) -> None:
        n = len(matrix)

        for row_idx in range(n):
            for col_idx in range(row_idx + 1, n):
                matrix[col_idx][row_idx], matrix[row_idx][col_idx] = (
                    matrix[row_idx][col_idx],
                    matrix[col_idx][row_idx],
                )

    def rotate(self, matrix: list[list[int]]) -> None:
        self.transpose(matrix)
        self.reflect(matrix)
