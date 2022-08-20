from typing import TypeAlias

from src.utils.binary_tree import TreeNode

Stack: TypeAlias = list[TreeNode | None]


class Solution:
    def isSameTree(self, p: TreeNode | None, q: TreeNode | None) -> bool:
        stack_p: Stack = [p]
        stack_q: Stack = [q]

        while stack_p and stack_q:
            node_p = stack_p.pop()
            node_q = stack_q.pop()

            if node_p and node_q:
                if node_p.val != node_q.val:
                    return False

                stack_p.append(node_p.left)
                stack_p.append(node_p.right)
                stack_q.append(node_q.left)
                stack_q.append(node_q.right)
            elif node_p is None and node_q is None:
                continue
            else:
                return False

        return not stack_p and not stack_q
