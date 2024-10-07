class Solution:
    @staticmethod
    def are_rows_valid(board: list[list[str]]) -> bool:
        for row in board:
            seen: set[str] = set()

            for x in row:
                if x != ".":
                    if x in seen:
                        return False
                    seen.add(x)
        return True

    @staticmethod
    def are_cols_valid(board: list[list[str]]) -> bool:
        for c in range(9):
            seen: set[str] = set()

            for r in range(9):
                if (x := board[r][c]) != ".":
                    if x in seen:
                        return False
                    seen.add(x)
        return True

    @staticmethod
    def are_squares_valid(board: list[list[str]]) -> bool:
        for sr in range(3):
            for sc in range(3):
                seen: set[str] = set()

                for r in range(3):
                    for c in range(3):
                        if (x := board[r + 3 * sr][c + 3 * sc]) != ".":
                            if x in seen:
                                return False
                            seen.add(x)
        return True

    def isValidSudoku(self, board: list[list[str]]) -> bool:
        return (
            self.are_rows_valid(board)
            and self.are_cols_valid(board)
            and self.are_squares_valid(board)
        )
