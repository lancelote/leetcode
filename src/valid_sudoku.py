from collections.abc import Iterator
from itertools import chain


def to_int_seq(seq: list[str]) -> list[int]:
    return [int(x) for x in seq if x != "."]


def rows(board: list[list[str]]) -> Iterator[list[int]]:
    for row in board:
        yield to_int_seq(row)


def cols(board: list[list[str]]) -> Iterator[list[int]]:
    for col_i in range(9):
        col = [row[col_i] for row in board]
        yield to_int_seq(col)


def squares(board: list[list[str]]) -> Iterator[list[int]]:
    for i in range(3):
        for j in range(3):
            square = [board[3 * i + k // 3][3 * j + k % 3] for k in range(9)]
            yield to_int_seq(square)


class Solution:
    def isValidSudoku(self, board: list[list[str]]) -> bool:
        for seq in chain(rows(board), cols(board), squares(board)):
            if len(seq) != len(set(seq)):
                return False
        return True
