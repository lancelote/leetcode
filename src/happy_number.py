def sum_of_squares_of_digits(n: int) -> int:
    return sum(int(x) * int(x) for x in str(n))


class Solution:
    def isHappy(self, n: int) -> bool:
        cache: set[int] = set()

        while n != 1:
            if n in cache:
                return False
            cache.add(n)
            n = sum_of_squares_of_digits(n)

        return True
