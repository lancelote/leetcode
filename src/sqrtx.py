class Solution:
    def mySqrt(self, x: int) -> int:
        left, right = 0, x

        while left <= right:
            middle = left + (right - left) // 2

            if middle * middle <= x:
                left = middle + 1
            else:
                right = middle - 1

        return right
