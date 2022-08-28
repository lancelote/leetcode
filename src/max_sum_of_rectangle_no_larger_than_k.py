import bisect


class Solution:
    def maxSumSubmatrix(self, matrix: list[list[int]], k: int) -> int | float:
        assert matrix
        assert matrix[0]

        rows = len(matrix)
        cols = len(matrix[0])

        rows_prefix_sum = [0] * rows
        max_sum = float("-inf")

        for left in range(cols):
            for i in range(rows):
                rows_prefix_sum[i] = 0

            for right in range(left, cols):
                current_list = [0]
                row_sum = 0

                for i in range(rows):
                    rows_prefix_sum[i] += matrix[i][right]
                    row_sum += rows_prefix_sum[i]
                    idx = bisect.bisect_left(current_list, row_sum - k)
                    if 0 <= idx < len(current_list):
                        max_sum = max(max_sum, row_sum - current_list[idx])
                    bisect.insort(current_list, row_sum)

        return max_sum
