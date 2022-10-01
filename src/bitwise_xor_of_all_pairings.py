class Solution:
    def xorAllNums(self, nums1: list[int], nums2: list[int]) -> int:
        nums1_ones = [0] * 30
        nums2_ones = [0] * 30

        for i in range(30):
            mask = 1 << i

            for num1 in nums1:
                if num1 & mask == mask:
                    nums1_ones[-i - 1] += 1

            for num2 in nums2:
                if num2 & mask == mask:
                    nums2_ones[-i - 1] += 1

        nums1_zeros = [len(nums1) - x for x in nums1_ones]
        nums2_zeros = [len(nums2) - x for x in nums2_ones]

        # How many ones will be in XOR results for each bit
        result = [
            a * d + b * c
            for a, b, c, d in zip(
                nums1_zeros, nums1_ones, nums2_zeros, nums2_ones
            )
        ]

        # If number of ones is odd - XOR will be 1
        result = [1 if x % 2 == 1 else 0 for x in result]

        return int("".join(str(x) for x in result), base=2)
