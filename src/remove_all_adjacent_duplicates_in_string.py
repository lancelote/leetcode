class Solution:
    def removeDuplicates(self, s: str) -> str:
        stack: list[str] = []

        for x in s:
            if not stack or stack[-1] != x:
                stack.append(x)
            elif stack[-1] == x:
                stack.pop()

        return "".join(stack)
