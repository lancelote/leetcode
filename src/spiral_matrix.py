import math


class Solution:
    def spiralOrder(self, matrix: list[list[int]]) -> list[int]:
        result: list[int] = []

        rows = len(matrix)
        cols = len(matrix[0])

        layers = math.ceil(min(rows, cols) / 2)

        for layer in range(layers):

            # left to right
            for c in range(layer, cols - layer):
                result.append(matrix[layer][c])

            # top to bottom
            for r in range(layer + 1, rows - layer):
                result.append(matrix[r][cols - layer - 1])

            if layer == rows - layer - 1:
                break  # single row layer

            # right to left
            for c in range(cols - layer - 2, layer - 1, -1):
                result.append(matrix[rows - layer - 1][c])

            if layer == cols - layer - 1:
                break  # single column layer

            # bottom to top
            for r in range(rows - layer - 2, layer, -1):
                result.append(matrix[r][layer])

        return result
