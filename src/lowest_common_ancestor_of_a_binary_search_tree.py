from src.utils.binary_search_tree import TreeNode


class Solution:
    def lowestCommonAncestor(
        self, root: TreeNode, p: TreeNode, q: TreeNode
    ) -> TreeNode:
        if p.val > root.val and q.val > root.val:
            assert root.right
            return self.lowestCommonAncestor(root.right, p, q)
        elif p.val < root.val and q.val < root.val:
            assert root.left
            return self.lowestCommonAncestor(root.left, p, q)
        else:
            return root
