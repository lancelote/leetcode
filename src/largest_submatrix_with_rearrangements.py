class Solution:
    def largestSubmatrix(self, matrix: list[list[int]]) -> int:
        largest = 0

        for r in range(len(matrix)):
            for c in range(len(matrix[0])):
                if r != 0 and matrix[r][c] != 0:
                    matrix[r][c] += matrix[r - 1][c]

            sorted_row = sorted(matrix[r], reverse=True)

            for c in range(len(sorted_row)):
                largest = max(largest, sorted_row[c] * (c + 1))

        return largest
