class Solution:
    def maximalSquare(self, matrix: list[list[str]]) -> int:
        assert matrix

        total_rows = len(matrix)
        total_cols = len(matrix[0])
        cache: dict[tuple[int, int], int] = {}

        def max_len_of(r: int, c: int) -> int:
            if r >= total_rows or c >= total_cols:
                return 0

            if (r, c) not in cache:
                right = max_len_of(r, c + 1)
                diag = max_len_of(r + 1, c + 1)
                down = max_len_of(r + 1, c)

                cache[(r, c)] = 0
                if matrix[r][c] == "1":
                    cache[(r, c)] = 1 + min(right, diag, down)

            return cache[(r, c)]

        max_len_of(0, 0)
        max_len = max(cache.values())
        return max_len * max_len
