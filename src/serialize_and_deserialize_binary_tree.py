import re

from src.utils.binary_tree import TreeNode


class Codec:
    def serialize(self, root: TreeNode | None) -> str:
        result: list[int | None] = []

        def dfs(node: TreeNode | None) -> None:
            if not node:
                result.append(None)
            else:
                result.append(node.val)
                dfs(node.left)
                dfs(node.right)

        dfs(root)
        return ",".join("N" if x is None else str(x) for x in result)

    def deserialize(self, data: str) -> TreeNode | None:
        vals = (x.group(0) for x in re.finditer("-?[0-9]+|N", data))

        def dfs() -> TreeNode | None:
            val = next(vals)

            if val == "N":
                return None
            else:
                return TreeNode(int(val), left=dfs(), right=dfs())

        return dfs()
