from __future__ import annotations


class TreeNode:
    def __init__(
        self,
        val: int = 0,
        left: TreeNode | None = None,
        right: TreeNode | None = None,
    ) -> None:
        self.val = val
        self.left = left
        self.right = right


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
