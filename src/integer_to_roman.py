ROMAN_FIFTH = ["V", "L", "D"]
ROMAN_TENS = ["I", "X", "C", "M"]


class Solution:
    def intToRoman(self, num: int) -> str:
        result = []

        for i, x in enumerate(str(num)[::-1]):
            digit = int(x)

            if digit == 4:
                result.append(f"{ROMAN_TENS[i]}{ROMAN_FIFTH[i]}")
            elif digit == 9:
                result.append(f"{ROMAN_TENS[i]}{ROMAN_TENS[i + 1]}")
            elif digit < 4:
                result.append(ROMAN_TENS[i] * digit)
            else:
                result.append(ROMAN_FIFTH[i] + ROMAN_TENS[i] * (digit - 5))

        return "".join(result[::-1])
