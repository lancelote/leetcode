def reverse(num: int) -> int:
    return int(str(num)[::-1])


class Solution:
    def isSameAfterReversals(self, num: int) -> bool:
        return reverse(reverse(num)) == num
