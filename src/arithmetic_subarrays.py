def check_arithmetic_subarray(left: int, right: int, data: list[int]) -> bool:
    sorted_nums = sorted(data[i] for i in range(left, right + 1))
    step = sorted_nums[0] - sorted_nums[1]

    for i in range(1, len(sorted_nums) - 1):
        if sorted_nums[i] - sorted_nums[i + 1] != step:
            return False

    return True


class Solution:
    def checkArithmeticSubarrays(
        self,
        nums: list[int],
        left_ids: list[int],
        right_ids: list[int],
    ) -> list[bool]:
        result: list[bool] = []

        for left, right in zip(left_ids, right_ids):
            result.append(check_arithmetic_subarray(left, right, nums))

        return result
