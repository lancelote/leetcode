class Solution:
    def generate(self, num_rows: int) -> list[list[int]]:
        result: list[list[int]] = [[1]]

        for _ in range(num_rows - 1):
            row: list[int] = []

            for i in range(len(result[-1]) + 1):
                new_item = 0
                new_item += result[-1][i - 1] if 0 <= i - 1 else 0
                new_item += result[-1][i] if i < len(result[-1]) else 0
                row.append(new_item)

            result.append(row)

        return result
