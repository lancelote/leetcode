class Solution:
    def largestRectangleArea(self, heights: list[int]) -> int:
        n = len(heights)
        stack: list[tuple[int, int]] = []  # (height, start)
        largest = 0

        for i, height in enumerate(heights):
            old_i = i

            while stack and stack[-1][0] > height:
                old_height, old_i = stack.pop()
                largest = max(largest, old_height * (i - old_i))

            stack.append((height, old_i))

        for height, start in stack:
            largest = max(largest, height * (n - start))

        return largest
