class Solution:
    def interpret(self, command: str) -> str:
        al = False
        result = []

        for char in command:
            if char == "G":
                result.append(char)
            elif char == ")":
                if al:
                    result.append("al")
                    al = False
                else:
                    result.append("o")
            elif char == "a":
                al = True
        return "".join(result)
