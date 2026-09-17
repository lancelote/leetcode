from src.utils.binary_tree import TreeNode


def is_leaf(node: TreeNode) -> bool:
    return node.left is None and node.right is None


def path_to_str(path: list[int]) -> str:
    return "->".join(str(x) for x in path)


class Solution:
    def binaryTreePaths(self, root: TreeNode | None) -> list[str]:
        result: list[str] = []
        path: list[int] = []

        def dfs(node: TreeNode | None) -> None:
            if node is None:
                return

            path.append(node.val)

            if is_leaf(node):
                result.append(path_to_str(path))
            else:
                dfs(node.left)
                dfs(node.right)

            path.pop()

        dfs(root)
        return result
