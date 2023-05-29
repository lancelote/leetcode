from src.utils.binary_tree import TreeNode


class Solution:
    def inorderTraversal(self, root: TreeNode | None) -> list[int]:
        if not root:
            return []

        stack: list[TreeNode] = []
        result: list[int] = []
        current: TreeNode | None = root

        while current or stack:
            while current:
                stack.append(current)
                current = current.left
            current = stack.pop()
            result.append(current.val)
            current = current.right

        return result
