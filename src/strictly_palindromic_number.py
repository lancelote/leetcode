def is_palindrome(number: list[int]) -> bool:
    for i in range(len(number) // 2):
        if number[i] != number[-1 - i]:
            return False
    return True


def to_base(n: int, base: int) -> list[int]:
    result = []

    while n:
        result.append(int(n % base))
        n //= base

    return result


class Solution:
    def isStrictlyPalindromic(self, n: int) -> bool:
        for base in range(2, n - 1):
            num = to_base(n, base)
            if not is_palindrome(num):
                return False
        return True
