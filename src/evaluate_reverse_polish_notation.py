class Solution:
    def evalRPN(self, tokens: list[str]) -> int:
        stack: list[int] = []

        for token in tokens:
            try:
                stack.append(int(token))
            except ValueError:
                b = stack.pop()
                a = stack.pop()

                if token == "+":
                    stack.append(a + b)
                elif token == "-":
                    stack.append(a - b)
                elif token == "*":
                    stack.append(a * b)
                elif token == "/":
                    stack.append(int(a / b))
                else:
                    raise ValueError(f"unknown token: {token}")

        return stack[-1]
