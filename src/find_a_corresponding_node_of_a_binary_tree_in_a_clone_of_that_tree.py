from src.utils.binary_tree import TreeNode


class Solution:
    def getTargetCopy(
        self,
        original: TreeNode | None,
        cloned: TreeNode | None,
        target: TreeNode,
    ) -> TreeNode | None:
        if original and original.val == target.val:
            return cloned

        left = (
            self.getTargetCopy(original.left, cloned.left, target)
            if original and cloned
            else None
        )

        return (
            left or self.getTargetCopy(original.right, cloned.right, target)
            if original and cloned
            else None
        )
