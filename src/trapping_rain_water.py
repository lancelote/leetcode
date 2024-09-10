class Solution:
    def trap(self, height: list[int]) -> int:
        total_water = 0

        max_left = height[0]
        max_right = height[-1]

        li, ri = 0, len(height) - 1

        while ri - li > 1:
            if max_left <= max_right:
                water = min(max_left, max_right) - height[li + 1]
                li += 1
                max_left = max(max_left, height[li])
            else:
                water = min(max_left, max_right) - height[ri - 1]
                ri -= 1
                max_right = max(max_right, height[ri])

            total_water += max(0, water)

        return total_water
