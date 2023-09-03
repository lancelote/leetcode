from src.utils.binary_tree import TreeNode


class Solution:
    def preorderTraversal(self, root: TreeNode | None) -> list[int]:
        if not root:
            return []

        to_visit = [root]
        result: list[int] = []

        while to_visit:
            node = to_visit.pop()

            if node.right:
                to_visit.append(node.right)
            if node.left:
                to_visit.append(node.left)

            result.append(node.val)

        return result
