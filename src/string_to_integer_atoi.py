class Solution:
    def myAtoi(self, s: str) -> int:
        n = len(s)
        i = 0

        # skip space
        while i < n and s[i] == " ":
            i += 1

        sign = 1
        if i < n and s[i] == "-":
            sign = -1
            i += 1

        if sign == 1 and i < n and s[i] == "+":
            i += 1

        # skip zeros
        while i < n and s[i] == "0":
            i += 1

        result = 0
        while i < n:
            if not s[i].isnumeric():
                break

            result = result * 10 + ord(s[i]) - 48
            i += 1

        if sign == -1 and result > 2147483648:
            result = 2147483648
        elif sign == 1 and result > 2147483647:
            result = 2147483647

        return sign * result
