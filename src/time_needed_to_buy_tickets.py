class Solution:
    def timeRequiredToBuy(self, tickets: list[int], k: int) -> int:
        result = tickets[k]

        for i in range(k):
            result += min(tickets[k], tickets[i])

        for i in range(k + 1, len(tickets)):
            result += min(tickets[k] - 1, tickets[i])

        return result
