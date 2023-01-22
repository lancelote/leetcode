class Solution:
    def countDigits(self, num: int) -> int:
        count = 0

        for x in str(num):
            if num % int(x) == 0:
                count += 1

        return count
