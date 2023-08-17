from collections import deque
from typing import Deque


class Solution:
    def updateMatrix(self, mat: list[list[int]]) -> list[list[int]]:
        assert mat
        assert mat[0]

        rows = len(mat)
        cols = len(mat[0])

        stack: Deque[tuple[int, int, int]] = deque()

        for r in range(rows):
            for c in range(cols):
                if mat[r][c] == 0:
                    stack.append((r, c, 0))

        result = [[-1] * cols for _ in range(rows)]

        while stack:
            r, c, d = stack.popleft()

            if r < 0 or c < 0 or r >= rows or c >= cols:
                continue

            if result[r][c] == -1:
                result[r][c] = d

                stack.append((r + 1, c, d + 1))
                stack.append((r - 1, c, d + 1))
                stack.append((r, c + 1, d + 1))
                stack.append((r, c - 1, d + 1))

        return result
