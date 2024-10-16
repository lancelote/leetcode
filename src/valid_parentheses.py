PARENS = {
    "{": "}",
    "(": ")",
    "[": "]",
}


class Solution:
    def isValid(self, s: str) -> bool:
        stack: list[str] = []

        for x in s:
            if x in PARENS:
                stack.append(PARENS[x])
            else:
                if not stack or stack.pop() != x:
                    return False

        return not stack
