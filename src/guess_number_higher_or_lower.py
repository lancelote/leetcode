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
        left, right = 0, n

        while left <= right:
            middle = left + (right - left) // 2
            attempt = guess(middle)

            if attempt > 0:
                left = middle + 1
            elif attempt < 0:
                right = middle - 1
            else:
                return middle

        raise ValueError("no answer found")
