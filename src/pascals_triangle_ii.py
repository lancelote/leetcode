class Solution:
    def getRow(self, row_index: int) -> list[int]:
        row = [1]

        for _ in range(row_index):
            new_row = [1]

            for i in range(len(row)):
                new_item = row[i] + (row[i + 1] if i + 1 < len(row) else 0)
                new_row.append(new_item)

            row = new_row

        return row
