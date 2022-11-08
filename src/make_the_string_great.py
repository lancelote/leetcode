class Solution:
    def makeGood(self, s: str) -> str:
        stack: list[str] = []

        for x in s:
            if stack and x != stack[-1] and x.lower() == stack[-1].lower():
                stack.pop()
            else:
                stack.append(x)

        return "".join(stack)
