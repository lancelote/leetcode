ROMAN_TO_INT = {
    "I": 1,
    "V": 5,
    "X": 10,
    "L": 50,
    "C": 100,
    "D": 500,
    "M": 1000,
}


class Solution:
    def romanToInt(self, s: str) -> int:
        n = len(s)
        prev = result = ROMAN_TO_INT[s[0]]

        for i in range(1, n):
            x = ROMAN_TO_INT[s[i]]

            if x > prev:
                result += x - 2 * prev
            else:
                result += x
            prev = x

        return result
