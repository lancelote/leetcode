class Solution:
    def distMoney(self, money: int, children: int) -> int:
        if money < children:
            return -1
        if money - (children - 1) * 8 == 4:
            return children - 2
        if children * 8 < money:
            return children - 1
        return min((money - children) // 7, children)
