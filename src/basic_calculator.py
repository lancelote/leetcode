SIGN = {
    "+": +1,
    "-": -1,
}


class Solution:
    def calculate(self, s: str) -> int:
        current, sign, stack = 0, +1, [0]

        for x in s:
            if x.isdigit():
                current = current * 10 + int(x)
            elif x == " ":
                pass
            elif x in SIGN:
                stack[-1] += current * sign
                sign = SIGN[x]
                current = 0
            elif x == "(":
                stack.append(sign)
                stack.append(0)
                sign = 1
                current = 0
            elif x == ")":
                last = (stack.pop() + current * sign) * stack.pop()
                stack[-1] += last
                sign = 1
                current = 0
            else:
                raise ValueError(f"unknown token: {x}")

        return stack[-1] + current * sign
