class Solution:
    def trap(self, height: list[int]) -> int:
        result = 0

        max_left, max_right = 0, 0
        left, right = 0, len(height) - 1

        while left != right:
            if height[left] <= height[right]:
                result += max(0, max_left - height[left])
                max_left = max(max_left, height[left])
                left += 1
            else:
                result += max(0, max_right - height[right])
                max_right = max(max_right, height[right])
                right -= 1

        return result
