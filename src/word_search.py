class Solution:
    def exist(self, board: list[list[str]], word: str) -> bool:
        n_rows = len(board)
        n_cols = len(board[0])

        seen: set[tuple[int, int]] = set()

        def dfs(r: int, c: int, letter_idx: int = 0) -> bool:
            if letter_idx == len(word):
                return True

            if r < 0 or r >= n_rows or c < 0 or c >= n_cols:
                return False

            if word[letter_idx] != board[r][c]:
                return False

            if (r, c) in seen:
                return False

            seen.add((r, c))

            for dr, dc in (
                (-1, 0),
                (0, 1),
                (1, 0),
                (0, -1),
            ):
                nr = r + dr
                nc = c + dc

                if dfs(nr, nc, letter_idx + 1):
                    return True

            seen.discard((r, c))

            return False

        for row_idx, row in enumerate(board):
            for col_idx, letter in enumerate(row):
                if letter == word[0]:
                    if dfs(row_idx, col_idx):
                        return True

        return False
