class Solution:
    def mySqrt(self, x: int) -> int:
        left, right = 1, x

        while left <= right:
            middle = left + (right - left) // 2
            power = middle * middle

            if power == x:
                return middle
            elif power > x:
                right = middle - 1
            else:
                left = middle + 1

        return right
