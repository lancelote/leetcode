class Solution:
    def maximalRectangle(self, matrix: list[list[str]]) -> int:
        assert matrix
        assert matrix[0]

        n_rows = len(matrix)
        n_cols = len(matrix[0])

        height = [0] * n_cols
        left = [0] * n_cols
        right = [n_cols] * n_cols

        max_area = 0

        for r in range(n_rows):
            cur_left = 0
            cur_right = n_cols

            # height
            for c in range(n_cols):
                if matrix[r][c] == "1":
                    height[c] += 1
                else:
                    height[c] = 0

            # left
            for c in range(n_cols):
                if matrix[r][c] == "1":
                    left[c] = max(left[c], cur_left)
                else:
                    left[c] = 0
                    cur_left = c + 1

            # right
            for c in range(n_cols - 1, -1, -1):
                if matrix[r][c] == "1":
                    right[c] = min(right[c], cur_right)
                else:
                    right[c] = n_cols
                    cur_right = c

            # area
            for c in range(n_cols):
                max_area = max(max_area, height[c] * (right[c] - left[c]))

        return max_area
