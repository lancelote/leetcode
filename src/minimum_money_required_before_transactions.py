class Solution:
    def minimumMoney(self, transactions: list[list[int]]) -> int:
        total_loss = 0
        extra = 0

        for cost, cashback in transactions:
            if cost > cashback:
                total_loss += cost - cashback
            extra = max(extra, min(cost, cashback))

        return total_loss + extra
