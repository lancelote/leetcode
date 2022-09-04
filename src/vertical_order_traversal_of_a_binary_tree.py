import heapq
from collections import defaultdict

from src.utils.binary_tree import TreeNode


class Solution:
    def verticalTraversal(self, root: TreeNode | None) -> list[list[int]]:
        cols: dict[int, list[tuple[int, int]]] = defaultdict(list)

        def dfs(node: TreeNode | None, r: int, c: int) -> None:
            if node is None:
                return

            heapq.heappush(cols[c], (r, node.val))
            dfs(node.left, r + 1, c - 1)
            dfs(node.right, r + 1, c + 1)

        dfs(root, 0, 0)

        result = []
        for col_idx in sorted(cols.keys()):
            col = []
            while cols[col_idx]:
                _, val = heapq.heappop(cols[col_idx])
                col.append(val)
            result.append(col)

        return result
