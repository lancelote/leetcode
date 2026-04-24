from src.utils.binary_tree import TreeNode


class Solution:
    def dfs(self, node: TreeNode | None, target: float) -> tuple[float, int]:
        if node is None:
            return float("inf"), 0

        node_diff = abs(target - node.val)
        return min(
            (node_diff, node.val),
            self.dfs(node.left, target),
            self.dfs(node.right, target),
        )

    def closestValue(self, root: TreeNode | None, target: float) -> int:
        _, val = self.dfs(root, target)
        return val
