from itertools import combinations


class Solution:
    def maximumRows(self, mat: list[list[int]], cols: int) -> int:
        assert mat

        max_coverage = 0
        total_cols = len(mat[0])
        row_sums = [sum(row) for row in mat]

        for selected_cols in combinations(list(range(total_cols)), cols):
            row_sums_cache = [x for x in row_sums]

            for i, row in enumerate(mat):
                for selected_col in selected_cols:
                    if row[selected_col] == 1:
                        row_sums_cache[i] -= 1

            current_coverage = 0
            for x in row_sums_cache:
                if x == 0:
                    current_coverage += 1

            max_coverage = max(max_coverage, current_coverage)

        return max_coverage
