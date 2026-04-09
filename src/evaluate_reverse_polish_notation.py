class Solution:
    def evalRPN(self, tokens: list[str]) -> int:
        stack: list[int] = []

        for token in tokens:
            try:
                stack.append(int(token))
            except ValueError as e:
                b = stack.pop()
                a = stack.pop()

                match token:
                    case "+":
                        stack.append(a + b)
                    case "-":
                        stack.append(a - b)
                    case "*":
                        stack.append(a * b)
                    case "/":
                        stack.append(int(a / b))
                    case _:
                        raise ValueError(f"unknown token: {token}") from e

        return stack[0]
