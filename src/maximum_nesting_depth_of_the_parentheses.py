class Solution:
    def maxDepth(self, text: str) -> int:
        max_depth = current_depth = 0
        for letter in text:
            if letter == "(":
                current_depth += 1
                if current_depth > max_depth:
                    max_depth = current_depth
            elif letter == ")":
                current_depth -= 1
        return max_depth
