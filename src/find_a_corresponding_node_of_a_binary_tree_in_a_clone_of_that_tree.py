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

        assert original and cloned
        left = (
            self.getTargetCopy(original.left, cloned.left, target)
            if original
            else None
        )

        return (
            left or self.getTargetCopy(original.right, cloned.right, target)
            if original
            else None
        )
