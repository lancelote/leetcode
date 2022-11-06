from src.utils.binary_tree import TreeNode


class Solution:
    def inorderTraversal(self, root: TreeNode | None) -> list[int]:
        if not root:
            return []

        node: TreeNode | None = root
        traversal: list[int] = []
        stack: list[TreeNode] = []

        while node or stack:
            while node:
                stack.append(node)
                node = node.left
            node = stack.pop()
            traversal.append(node.val)
            node = node.right

        return traversal
