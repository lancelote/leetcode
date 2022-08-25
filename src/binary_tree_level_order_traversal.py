from src.utils.binary_tree import TreeNode


class Solution:
    def levelOrder(self, root: TreeNode | None) -> list[list[int]]:
        if not root:
            return []

        levels: list[list[int]] = []
        to_visit: list[TreeNode] = [root]

        while to_visit:
            new_to_visit: list[TreeNode] = []
            level: list[int] = []

            for node in to_visit:
                level.append(node.val)

                if node.left:
                    new_to_visit.append(node.left)
                if node.right:
                    new_to_visit.append(node.right)

            to_visit = new_to_visit
            levels.append(level)

        return levels
