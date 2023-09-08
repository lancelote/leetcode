class Solution:
    def generate(self, num_rows: int) -> list[list[int]]:
        result: list[list[int]] = [[1]]

        for _ in range(num_rows - 1):
            line: list[int] = []

            for i in range(len(result[-1]) + 1):
                left = result[-1][i - 1] if i - 1 >= 0 else 0
                right = result[-1][i] if i < len(result[-1]) else 0
                line.append(left + right)

            result.append(line)

        return result
