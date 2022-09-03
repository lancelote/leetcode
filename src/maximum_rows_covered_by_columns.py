from itertools import combinations


class Solution:
    def maximumRows(self, mat: list[list[int]], cols: int) -> int:
        assert mat

        max_coverage = 0
        total_cols = len(mat[0])

        for selected_cols in combinations(list(range(total_cols)), cols):
            masked = 0
            mask = sum(1 << col for col in selected_cols)

            for row in mat:
                bin_row = int("".join(str(x) for x in row), 2)
                if bin_row == bin_row & mask:
                    masked += 1

            max_coverage = max(max_coverage, masked)

        return max_coverage
