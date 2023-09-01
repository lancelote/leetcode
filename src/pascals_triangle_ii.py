class Solution:
    def getRow(self, row_index: int) -> list[int]:
        last_row = [1]

        for _ in range(row_index):
            new_row = []

            for i in range(len(last_row) + 1):
                item = 0
                item += last_row[i - 1] if 0 <= i - 1 else 0
                item += last_row[i] if i < len(last_row) else 0
                new_row.append(item)

            last_row = new_row

        return last_row
