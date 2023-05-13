class TreeNode:
    def __init__(self, x: int) -> None:
        self.val = x
        self.left: TreeNode | None = None
        self.right: TreeNode | None = None


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
