class Solution:
    def checkMove(
        self, board: list[list[str]], r: int, c: int, color: str
    ) -> bool:
        def check(shift_r, shift_c) -> bool:
            middle = False
            current_r, current_c = r + shift_r, c + shift_c

            while 0 <= current_r <= 7 and 0 <= current_c <= 7:
                current = board[current_r][current_c]

                if current == color and not middle:
                    return False
                elif current == color and middle:
                    return True
                elif current == ".":
                    return False
                elif current != color:
                    middle = True

                current_r += shift_r
                current_c += shift_c

            return False

        left = check(0, -1)
        right = check(0, +1)
        top = check(-1, 0)
        bottom = check(+1, 0)
        left_diagonal_top = check(-1, -1)
        left_diagonal_bottom = check(+1, +1)
        right_diagonal_top = check(-1, +1)
        right_diagonal_bottom = check(+1, -1)

        return any(
            [
                left,
                right,
                top,
                bottom,
                left_diagonal_top,
                left_diagonal_bottom,
                right_diagonal_top,
                right_diagonal_bottom,
            ]
        )
