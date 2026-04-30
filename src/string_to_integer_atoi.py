LIMIT = 214748364


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

            digit = ord(s[i]) - 48

            if result > LIMIT:
                return -2147483648 if sign == -1 else 2147483647
            elif result == LIMIT:
                if sign == -1 and digit > 8:
                    return -2147483648
                elif sign == 1 and digit > 7:
                    return 2147483647

            result = result * 10 + digit
            i += 1

        return sign * result
