from enum import Enum


class Angle(Enum):
    TOP = 0
    RIGHT = 1
    LEFT = 2


class Solution:
    def findBall(self, grid: list[list[int]]) -> list[int]:
        assert grid
        assert grid[0]

        rows = len(grid)
        cols = len(grid[0])

        answer: list[int] = []
        cache: dict[tuple[int, int, Angle], int] = {}

        def falls(r: int, c: int, angle: Angle) -> int:
            if (r, c, angle) in cache:
                return cache[(r, c, angle)]

            if r < 0 or c < 0 or c >= cols:
                result = -1
            elif r >= rows:
                result = c
            elif angle is Angle.TOP:
                if grid[r][c] == 1:
                    result = falls(r, c + 1, Angle.RIGHT)
                else:
                    result = falls(r, c - 1, Angle.LEFT)
            elif angle is Angle.RIGHT:
                if grid[r][c] == 1:
                    result = falls(r + 1, c, Angle.TOP)
                else:
                    result = -1
            else:
                if grid[r][c] == 1:
                    result = -1
                else:
                    result = falls(r + 1, c, Angle.TOP)

            cache[(r, c, angle)] = result
            return result

        for start in range(cols):
            answer.append(falls(r=0, c=start, angle=Angle.TOP))

        return answer
