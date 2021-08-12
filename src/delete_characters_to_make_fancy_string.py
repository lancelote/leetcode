class Solution:
    def makeFancyString(self, string: str) -> str:
        filtered_string = []

        equal_count = 0
        last = ""

        for char in string:
            if char != last:
                last = char
                equal_count = 0
                filtered_string.append(char)
            elif equal_count == 0:
                equal_count += 1
                filtered_string.append(char)
            elif equal_count == 1:
                pass

        return "".join(filtered_string)
