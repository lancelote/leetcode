class Solution:
    def trap(self, height: list[int]) -> int:
        n = len(height)

        current_max_left = 0
        max_left = []

        for x in height:
            max_left.append(current_max_left)
            current_max_left = max(current_max_left, x)

        current_max_right = 0
        max_right = [0] * n

        for i in range(n - 1, -1, -1):
            max_right[i] = current_max_right
            current_max_right = max(current_max_right, height[i])

        min_border = [min(x, y) for x, y in zip(max_left, max_right)]
        result = sum(x - y for x, y in zip(min_border, height) if x - y > 0)

        return result
