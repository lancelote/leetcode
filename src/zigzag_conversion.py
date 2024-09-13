class Solution:
    def convert(self, s: str, num_rows: int) -> str:
        if num_rows == 1:
            return s

        n = len(s)
        result: list[str] = []

        step = (num_rows - 1) * 2

        # first row
        for i in range(0, n, step):
            result.append(s[i])

        # middle rows
        for r in range(1, num_rows - 1):
            for i in range(r, n, step):
                result.append(s[i])

                j = i + (step - r * 2)
                if j < n:
                    result.append(s[j])

        # last row
        for i in range(num_rows - 1, n, step):
            result.append(s[i])

        return "".join(result)
