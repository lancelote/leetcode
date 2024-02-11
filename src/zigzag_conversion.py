class Solution:
    def convert(self, s: str, num_rows: int) -> str:
        data: list[list[str]] = [[] for _ in range(num_rows)]

        i = 0
        shift = +1

        for x in s:
            data[i].append(x)
            i = (i + shift) % num_rows

            if i == 0 or i == num_rows - 1:
                shift *= -1

        return "".join("".join(x) for x in data)
