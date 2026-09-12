class Solution:
    def convertToTitle(self, column_number: int) -> str:
        result: list[str] = []

        while column_number > 0:
            column_number -= 1
            digit = column_number % 26
            column_number //= 26

            result.append(chr(digit + ord('A')))

        return "".join(result[::-1])
