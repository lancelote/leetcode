class Solution:
    def minimumRecolors(self, blocks: str, k: int) -> int:
        ws = 0

        blocks_iter = iter(blocks)
        for _ in range(k):
            next_block = next(blocks_iter)
            if next_block == "W":
                ws += 1

        min_ws = ws

        for i, next_block in enumerate(blocks_iter):
            if next_block == "W":
                ws += 1

            if blocks[i] == "W":
                ws -= 1

            min_ws = min(min_ws, ws)

        return min_ws
