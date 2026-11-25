class Solution:
    def isPerfectSquare(self, num: int) -> bool:
        left, right = 0, num

        while left <= right:
            middle = left + (right - left) // 2
            guess = middle * middle

            if guess == num:
                return True
            elif guess < num:
                left = middle + 1
            else:
                right = middle - 1

        return False
