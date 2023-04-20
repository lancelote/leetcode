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
    def isBalanced(self, root: TreeNode | None) -> bool:
        def get_depth(node: TreeNode | None, depth: int) -> int:
            if node is None:
                return depth

            left = get_depth(node.left, depth + 1)
            right = get_depth(node.right, depth + 1)

            if abs(left - right) > 1:
                raise ValueError
            else:
                return max(left, right)

        try:
            get_depth(root, 0)
        except ValueError:
            return False
        return True
