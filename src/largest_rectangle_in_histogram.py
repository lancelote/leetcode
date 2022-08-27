class Solution:
    def largestRectangleArea(self, heights: list[int]) -> int:
        assert heights

        max_area = 0
        stack: list[tuple[int, int]] = []

        for i, x in enumerate(heights):
            old_i = i

            while stack and heights[i] < stack[-1][1]:
                old_i, old_height = stack.pop()
                area = (i - old_i) * old_height
                max_area = max(max_area, area)

            stack.append((old_i, heights[i]))

        while stack:
            old_i, old_height = stack.pop()
            area = (len(heights) - old_i) * old_height
            max_area = max(max_area, area)

        return max_area
