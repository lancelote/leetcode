class Solution:
    def numberOfSteps(self, num: int) -> int:
        digits = bin(num)[2:]
        return digits.count("1") + len(digits) - 1
