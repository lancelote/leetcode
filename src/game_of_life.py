SHIFTS = (
    (-1, -1),
    (-1, 0),
    (-1, +1),
    (0, +1),
    (+1, +1),
    (+1, 0),
    (+1, -1),
    (0, -1),
)


def get_count(board: list[list[int]], r: int, c: int) -> int:
    rows = len(board)
    cols = len(board[0])

    count = 0

    for dr, dc in SHIFTS:
        new_r = r + dr
        new_c = c + dc

        if 0 <= new_r < rows and 0 <= new_c < cols:
            new_value = board[new_r][new_c]

            if new_value == 1 or new_value == 3:
                count += 1

    return count


class Solution:
    def gameOfLife(self, board: list[list[int]]) -> None:
        for r in range(len(board)):
            for c in range(len(board[0])):
                value = board[r][c]
                count = get_count(board, r, c)

                if count < 2:  # dies if alive
                    if value == 1:
                        board[r][c] = 1
                elif count < 3:  # lives if alive
                    if value == 1:
                        board[r][c] = 3
                elif count == 3:  # becomes alive if dead
                    if value == 0:
                        board[r][c] = 2
                    elif value == 1:
                        board[r][c] = 3
                else:  # dies
                    if value == 1:
                        board[r][c] = 1

        for r, row in enumerate(board):
            for c, value in enumerate(row):
                if value == 2 or value == 3:
                    board[r][c] = 1
                elif value == 1:
                    board[r][c] = 0
