class Solution:
    def findDuplicate(self, nums: list[int]) -> int:
        slow1 = slow2 = fast = nums[0]

        while True:
            slow1 = nums[slow1]
            fast = nums[fast]
            fast = nums[fast]

            if slow1 == fast:
                break

        while slow1 != slow2:
            slow1 = nums[slow1]
            slow2 = nums[slow2]

        return slow1
