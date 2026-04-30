import math


class Solution:
    def accountBalanceAfterPurchase(self, purchase_amount: int) -> int:
        if purchase_amount % 5 == 0:
            left = (purchase_amount // 10) * 10
            right = math.ceil(purchase_amount / 10) * 10
            return 100 - max(left, right)
        elif purchase_amount % 10 < 5:
            return 100 - (purchase_amount // 10) * 10
        else:
            return 100 - math.ceil(purchase_amount / 10) * 10
