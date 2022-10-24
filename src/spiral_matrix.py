class Solution:
    def spiralOrder(self, matrix: list[list[int]]) -> list[int]:
        result: list[int] = []

        left = 0
        right = len(matrix[0])
        top = 0
        bottom = len(matrix)

        while left < right and top < bottom:
            for c in range(left, right):
                result.append(matrix[top][c])
            top += 1

            for r in range(top, bottom):
                result.append(matrix[r][right - 1])
            right -= 1

            if not (left < right and top < bottom):
                break

            for c in range(right - 1, left - 1, -1):
                result.append(matrix[bottom - 1][c])
            bottom -= 1

            for r in range(bottom - 1, top - 1, -1):
                result.append(matrix[r][left])
            left += 1

        return result
