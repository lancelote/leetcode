import typing as t
from collections import Counter

from src.utils.binary_tree import TreeNode


class Solution:
    def findMode(self, root: TreeNode | None) -> list[int]:
        counter: t.Counter[int] = Counter()

        def dfs(node: TreeNode | None) -> None:
            if node is None:
                return

            counter[node.val] += 1

            dfs(node.left)
            dfs(node.right)

        dfs(root)

        result: list[int] = []

        [(_, most_common)] = counter.most_common(1)

        for x, count in counter.most_common():
            if count == most_common:
                result.append(x)
            else:
                break

        return result
