class Solution:
    def champagneTower(self, poured: int, qr: int, qc: int) -> float:
        dp: list[list[float]] = [[0] * i for i in range(1, 101)]
        dp[0][0] = poured

        for r in range(99):
            for c in range(r + 1):
                flow = (dp[r][c] - 1) / 2

                if flow > 0:
                    dp[r + 1][c] += flow
                    dp[r + 1][c + 1] += flow

        return min(1.0, dp[qr][qc])
