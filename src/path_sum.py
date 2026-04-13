from src.utils.binary_tree import TreeNode


class Solution:
    def hasPathSum(self, root: TreeNode | None, target_sum: int) -> bool:
        if (
            root is not None
            and target_sum - root.val == 0
            and root.left is None
            and root.right is None
        ):
            return True

        if root is None:
            return False

        new_sum = target_sum - root.val
        return self.hasPathSum(root.left, new_sum) or self.hasPathSum(
            root.right, new_sum
        )
