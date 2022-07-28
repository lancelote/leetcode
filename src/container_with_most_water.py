class Solution:
    def maxArea(self, height: list[int]) -> int:
        left = 0
        right = len(height) - 1
        max_amount = 0

        while left < right:
            left_value = height[left]
            right_value = height[right]

            amount = min(left_value, right_value) * (right - left)
            max_amount = max(max_amount, amount)

            if left_value > right_value:
                right -= 1
            else:
                left += 1

        return max_amount
