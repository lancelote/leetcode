from src.utils.binary_tree import TreeNode


class Solution:
    def lowestCommonAncestor(
        self, root: TreeNode, p: TreeNode, q: TreeNode
    ) -> TreeNode | None:
        result = None

        def search(node: TreeNode | None) -> bool:
            nonlocal result

            if node is None:
                return False

            left = search(node.left)
            right = search(node.right)
            middle = node.val == p.val or node.val == q.val

            if middle + left + right >= 2:
                result = node

            return left or right or middle

        search(root)
        return result
