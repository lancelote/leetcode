SHIFTS = [
    (-1, 0),
    (0, +1),
    (+1, 0),
    (0, -1),
]


class Solution:
    def exist(self, board: list[list[str]], word: str) -> bool:
        assert word
        assert board
        assert board[0]

        rows = len(board)
        cols = len(board[0])

        def find(i: int, r: int, c: int) -> bool:
            if i == len(word):
                return True

            if r < 0 or r >= rows or c < 0 or c >= cols:
                return False

            if word[i] != board[r][c]:
                return False

            if not board[r][c]:
                return False

            tmp = board[r][c]
            board[r][c] = ""

            for dr, dc in SHIFTS:
                if find(i + 1, r + dr, c + dc):
                    return True

            board[r][c] = tmp
            return False

        for r, row in enumerate(board):
            for c, x in enumerate(row):
                if x == word[0]:
                    if find(0, r, c):
                        return True

        return False
