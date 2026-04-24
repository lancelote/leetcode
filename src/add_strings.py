class Solution:
    def addStrings(self, num1: str, num2: str) -> str:
        result: list[str] = []

        i1 = len(num1) - 1
        i2 = len(num2) - 1

        carry = 0

        while i1 >= 0 or i2 >= 0:
            x1 = ord(num1[i1]) - ord("0") if i1 >= 0 else 0
            x2 = ord(num2[i2]) - ord("0") if i2 >= 0 else 0

            x = x1 + x2 + carry
            result.append(str(x % 10))
            carry = x // 10

            i1 -= 1
            i2 -= 1

        if carry == 1:
            result.append(str(carry))

        return "".join(result[::-1])
