from src.utils.binary_tree import TreeNode


class Solution:
    def averageOfLevels(self, root: TreeNode | None) -> list[float]:
        assert root
        level: list[TreeNode] = [root]
        result: list[float] = []

        while level:
            level_sum = 0
            new_level: list[TreeNode] = []

            for node in level:
                level_sum += node.val
                if node.left:
                    new_level.append(node.left)
                if node.right:
                    new_level.append(node.right)

            level_average = level_sum / len(level)
            result.append(level_average)
            level = new_level

        return result
