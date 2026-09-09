from math import ceil


class Solution:
    def spiralOrder(self, matrix: list[list[int]]) -> list[int]:
        n_rows = len(matrix)
        n_cols = len(matrix[0])
        n_layers = min(ceil(n_rows / 2), ceil(n_cols / 2))

        elements: list[int] = []

        for layer_idx in range(n_layers):
            # top
            for col_idx in range(layer_idx, n_cols - layer_idx):
                elements.append(matrix[layer_idx][col_idx])

            if layer_idx == n_rows - layer_idx - 1:
                break  # single row layer

            # right
            for row_idx in range(layer_idx + 1, n_rows - layer_idx):
                elements.append(matrix[row_idx][n_cols - layer_idx - 1])

            if layer_idx == n_cols - layer_idx - 1:
                break  # single column layer

            # bottom
            for col_idx in range(n_cols - layer_idx - 2, layer_idx - 1, -1):
                elements.append(matrix[n_rows - layer_idx - 1][col_idx])

            # left
            for row_idx in range(n_rows - layer_idx - 2, layer_idx, -1):
                elements.append(matrix[row_idx][layer_idx])

        return elements
