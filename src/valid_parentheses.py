PARENTHESES = {
    "(": ")",
    "{": "}",
    "[": "]",
}


class Solution:
    def isValid(self, text: str) -> bool:
        stack = []
        for char in text:
            if char in PARENTHESES.keys():
                stack.append(char)
            elif stack:
                last = stack.pop()
                if PARENTHESES.get(last) != char:
                    return False
            else:
                return False
        return len(stack) == 0
