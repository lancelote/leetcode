class Solution:
    def subtractProductAndSum(self, number: int) -> int:
        product_of_digits = 1
        sum_of_digits = 0

        while number:
            digit = number % 10

            product_of_digits *= digit
            sum_of_digits += digit

            number //= 10

        return product_of_digits - sum_of_digits
