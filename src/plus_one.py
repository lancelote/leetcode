class Solution:
    def plusOne(self, digits: list[int]) -> list[int]:
        for i in range(len(digits) - 1, -1, -1):
            digits[i] = (digits[i] + 1) % 10
            if digits[i] != 0:
                break

        if digits[0] == 0:
            digits = [1, *digits]

        return digits
