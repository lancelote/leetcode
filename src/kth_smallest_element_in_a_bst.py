from src.utils.binary_search_tree import TreeNode


class Solution:
    def kthSmallest(self, root: TreeNode | None, k: int) -> int:
        stack: list[TreeNode] = []
        found = 0

        while found < k:
            if not root:
                last = stack.pop()
                found += 1
                if found == k:
                    return last.val
                root = last.right
            else:
                stack.append(root)
                root = root.left

        raise ValueError
