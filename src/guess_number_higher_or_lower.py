import os


def guess(num: int) -> int:
    secret = int(os.environ["SECRET"])

    if num > secret:
        return -1
    elif num < secret:
        return 1
    else:
        return 0


class Solution:
    def guessNumber(self, n: int) -> int:
        left, right = 1, n

        while left <= right:
            middle = (right - left) // 2 + left
            attempt = guess(middle)
            if attempt == -1:
                right = middle - 1
            elif attempt == 1:
                left = middle + 1
            else:
                return middle

        raise ValueError
