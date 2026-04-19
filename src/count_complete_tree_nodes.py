from src.utils.binary_tree import TreeNode


class Solution:
    def get_depth(self, root: TreeNode | None) -> int:
        d = 0
        while root is not None:
            d += 1
            root = root.left

        return d

    def exists(self, idx: int, d: int, node: TreeNode | None) -> bool:
        left, right = 0, 2 ** (d - 1)

        for _ in range(d - 1):
            assert node is not None

            middle = left + (right - left) // 2

            if idx < middle:
                node = node.left
                right = middle
            else:
                node = node.right
                left = middle + 1

        return node is not None

    def countNodes(self, root: TreeNode | None) -> int:
        if root is None:
            return 0

        d = self.get_depth(root)
        if d == 1:
            return 1

        left, right = 0, 2 ** (d - 1) - 1
        while left <= right:
            middle = left + (right - left) // 2
            if self.exists(middle, d, root):
                left = middle + 1
            else:
                right = middle - 1

        return 2 ** (d - 1) - 1 + left
