class Solution:
    def searchMatrix(self, matrix: list[list[int]], target: int) -> bool:
        # find row
        top = 0
        bottom = len(matrix) - 1

        while top <= bottom:
            row = top + (bottom - top) // 2

            if target > matrix[row][-1]:
                top = row + 1
            elif target < matrix[row][0]:
                bottom = row - 1
            else:
                break
        else:
            return False

        # find column
        left = 0
        right = len(matrix[row]) - 1

        while left <= right:
            middle = left + (right - left) // 2

            if target > matrix[row][middle]:
                left = middle + 1
            elif target < matrix[row][middle]:
                right = middle - 1
            else:
                return True

        return False
