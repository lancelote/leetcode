class Solution:
    def maximumScore(self, nums: list[int], k: int) -> int:
        li = ri = k
        max_score = min_so_far = nums[k]

        while li > 0 or ri < len(nums) - 1:
            left = nums[li - 1] if li > 0 else 0
            right = nums[ri + 1] if ri < len(nums) - 1 else 0

            if left > right:
                li -= 1
                min_so_far = min(min_so_far, left)
            else:
                ri += 1
                min_so_far = min(min_so_far, right)

            max_score = max(max_score, min_so_far * (ri - li + 1))

        return max_score
