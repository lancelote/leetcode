TOP_LIMIT = 2**31 - 1
BOTTOM_LIMIT = -(2**31)


class Solution:
    def myAtoi(self, s: str) -> int:
        num = 0
        s = s.lstrip()

        digits: list[str] = []

        start = 0
        if s and s[0] in {"+", "-"}:
            start = 1

        for i in range(start, len(s)):
            if not s[i].isdigit():
                break
            digits.append(s[i])

        if digits:
            num += int("".join(digits))

        if s and s[0] == "-":
            num *= -1

        if num < BOTTOM_LIMIT:
            num = BOTTOM_LIMIT
        elif num > TOP_LIMIT:
            num = TOP_LIMIT

        return num
