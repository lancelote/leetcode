class Solution:
    def winnerOfGame(self, colors: str) -> bool:
        n = len(colors)

        alice = 0
        bob = 0

        for i in range(1, n - 1):
            if colors[i - 1] == colors[i] == colors[i + 1] == "A":
                alice += 1
            elif colors[i - 1] == colors[i] == colors[i + 1] == "B":
                bob += 1

        return alice > bob
