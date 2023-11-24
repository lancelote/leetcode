from collections import deque


class Solution:
    def findDiagonalOrder(self, nums: list[list[int]]) -> list[int]:
        result: list[int] = []
        d = deque(((0, 0),))

        while d:
            r, c = d.popleft()
            result.append(nums[r][c])

            if c == 0 and r + 1 < len(nums):
                d.append((r + 1, c))
            if c + 1 < len(nums[r]):
                d.append((r, c + 1))

        return result
