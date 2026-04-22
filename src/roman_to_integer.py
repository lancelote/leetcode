TO_INT: dict[str, int] = {
    "M": 1000,
    "D": 500,
    "C": 100,
    "L": 50,
    "X": 10,
    "V": 5,
    "I": 1,
}


class Solution:
    def romanToInt(self, s: str) -> int:
        total = TO_INT[s[-1]]

        for i in range(len(s) - 1):
            if TO_INT[s[i]] < TO_INT[s[i + 1]]:
                total -= TO_INT[s[i]]
            else:
                total += TO_INT[s[i]]

        return total
