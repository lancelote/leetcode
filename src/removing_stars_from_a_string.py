class Solution:
    def removeStars(self, s: str) -> str:
        stack: list[str] = []

        for x in s:
            if x == "*":
                stack.pop()
            else:
                stack.append(x)

        return "".join(stack)
