from src.utils.binary_tree import TreeNode


class Solution:
    def closestValue(self, root: TreeNode | None, target: float) -> int:
        assert root is not None

        closest = root.val

        while root:
            closest = min(closest, root.val, key=lambda x: (abs(target - x), x))
            root = root.left if target < root.val else root.right

        return closest
