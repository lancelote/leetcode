import sys


class Solution:
    def find132pattern(self, nums: list[int]) -> bool:
        stack: list[tuple[int, int]] = []
        min_so_far = sys.maxsize

        for x in nums:
            while stack and stack[-1][0] <= x:
                stack.pop()

            if stack and stack[-1][1] < x < stack[-1][0]:
                return True

            stack.append((x, min_so_far))
            min_so_far = min(min_so_far, x)

        return False
