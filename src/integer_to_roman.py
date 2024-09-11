INT_TO_ROMAN = {
    1000: "M",
    900: "CM",
    500: "D",
    400: "CD",
    100: "C",
    90: "XC",
    50: "L",
    40: "XL",
    10: "X",
    9: "IX",
    5: "V",
    4: "IV",
    1: "I",
}

INTEGERS = sorted(INT_TO_ROMAN.keys(), reverse=True)


class Solution:
    def intToRoman(self, num: int) -> str:
        result: list[str] = []

        while num:
            for integer in INTEGERS:
                while num >= integer:
                    result.append(INT_TO_ROMAN[integer])
                    num -= integer

        return "".join(result)
