class Solution:
    def removeOuterParentheses(self, text: str) -> str:
        count = 0
        result: list[str] = []

        for letter in text:
            if letter == "(" and count > 0:
                result.append(letter)
            elif letter == ")" and count > 1:
                result.append(letter)

            if letter == "(":
                count += 1
            else:
                count -= 1

        return "".join(result)
