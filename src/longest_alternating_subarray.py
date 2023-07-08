class Solution:
    def alternatingSubarray(self, nums: list[int]) -> int:
        assert len(nums) > 1

        max_len = 1
        cur_len = 1
        coef = +1

        for i in range(len(nums) - 1):
            if nums[i] + coef == nums[i + 1]:
                coef *= -1
                cur_len += 1
            elif nums[i] + 1 == nums[i + 1]:
                cur_len = 2
                coef = -1
            else:
                cur_len = 1
                coef = +1

            max_len = max(max_len, cur_len)

        max_len = max(max_len, cur_len)
        return max_len if max_len != 1 else -1
