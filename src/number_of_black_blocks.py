class Solution:
    def countBlackBlocks(
        self, m: int, n: int, coordinates: list[list[int]]
    ) -> list[int]:
        coors = {tuple(x) for x in coordinates}

        total = (m - 1) * (n - 1)
        result = [0] * 5

        for x, y in coordinates:
            # top-left
            if x != 0 and y != 0:
                tl = sum(
                    [
                        (x - 1, y - 1) in coors,
                        (x - 1, y) in coors,
                        (x, y - 1) in coors,
                        1,
                    ]
                )
                result[tl] += 1

            # top-right
            if x != 0 and y != n - 1:
                tr = sum(
                    [
                        (x - 1, y) in coors,
                        (x - 1, y + 1) in coors,
                        (x, y + 1) in coors,
                        1,
                    ]
                )
                result[tr] += 1

            # bottom-left
            if x != m - 1 and y != 0:
                bl = sum(
                    [
                        (x, y - 1) in coors,
                        1,
                        (x + 1, y) in coors,
                        (x + 1, y - 1) in coors,
                    ]
                )
                result[bl] += 1

            # bottom-right
            if x != m - 1 and y != n - 1:
                br = sum(
                    [
                        1,
                        (x, y + 1) in coors,
                        (x + 1, y + 1) in coors,
                        (x + 1, y) in coors,
                    ]
                )
                result[br] += 1

        result[2] = result[2] // 2
        result[3] = result[3] // 3
        result[4] = result[4] // 4
        result[0] = total - sum(result)
        return result
