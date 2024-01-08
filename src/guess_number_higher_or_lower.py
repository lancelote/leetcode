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
            middle = (left + right) // 2
            match guess(middle):
                case 0:
                    return middle
                case -1:
                    right = middle - 1
                case 1:
                    left = middle + 1
                case _:
                    raise ValueError("unexpected API answer")

        raise ValueError("answer not found")
