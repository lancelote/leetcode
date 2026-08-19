class Solution:
    def is_sequence_valid(self, sequence: list[str]) -> bool:
        seen: set[str] = set()

        for item in sequence:
            if item != "." and item in seen:
                return False
            seen.add(item)

        return True

    def are_rows_valid(self, board: list[list[str]]) -> bool:
        for row in board:
            if not self.is_sequence_valid(row):
                return False

        return True

    def are_cols_valid(self, board: list[list[str]]) -> bool:
        for col_idx in range(9):
            col: list[str] = []

            for row_idx in range(9):
                col.append(board[row_idx][col_idx])

            if not self.is_sequence_valid(col):
                return False

        return True

    def are_squares_valid(self, board: list[list[str]]) -> bool:
        for square_col_idx in range(3):
            for square_row_idx in range(3):
                square: list[str] = []

                for col_idx in range(3):
                    for row_idx in range(3):
                        c = col_idx + square_col_idx * 3
                        r = row_idx + square_row_idx * 3
                        square.append(board[r][c])

                if not self.is_sequence_valid(square):
                    return False

        return True

    def isValidSudoku(self, board: list[list[str]]) -> bool:
        return (
            self.are_rows_valid(board)
            and self.are_cols_valid(board)
            and self.are_squares_valid(board)
        )
