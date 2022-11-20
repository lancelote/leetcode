class Solution:
    def calculate(self, s: str) -> int:
        num, sign, stack = 0, 1, [0]

        for x in s:
            if x.isnumeric():
                num = num * 10 + int(x)
            elif x == " ":
                continue
            elif x == "+":
                stack[-1] += num * sign
                sign = 1
                num = 0
            elif x == "-":
                stack[-1] += num * sign
                sign = -1
                num = 0
            elif x == "(":
                stack.extend([sign, 0])
                sign = 1
                num = 0
            elif x == ")":
                last = (stack.pop() + num * sign) * stack.pop()
                stack[-1] += last
                sign = 1
                num = 0
            else:
                raise ValueError("unknown token: {x}")

        return stack[-1] + num * sign
