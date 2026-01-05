from __future__ import annotations

from src.utils.binary_tree import TreeNode


class Solution:
    def sortedArrayToBST(self, nums: list[int]) -> TreeNode | None:
        def construct_tree(left: int, right: int) -> TreeNode | None:
            if left >= right:
                return None

            middle = (right - left) // 2 + left
            return TreeNode(
                val=nums[middle],
                left=construct_tree(left, middle),
                right=construct_tree(middle + 1, right),
            )

        return construct_tree(0, len(nums))
