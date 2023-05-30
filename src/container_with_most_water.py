class Solution:
    def maxArea(self, height: list[int]) -> int:
        left = 0
        right = len(height) - 1
        biggest_area = 0

        while left < right:
            left_bar = height[left]
            right_bar = height[right]
            current_area = min(left_bar, right_bar) * (right - left)
            biggest_area = max(biggest_area, current_area)

            if left_bar < right_bar:
                left += 1
            else:
                right -= 1

        return biggest_area
