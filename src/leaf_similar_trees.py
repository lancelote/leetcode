from collections.abc import Iterator
from itertools import zip_longest

from src.utils.binary_tree import TreeNode


def leaf_value_seq(root: TreeNode | None) -> Iterator[int]:
    if not root:
        raise StopIteration

    stack = [root]

    while stack:
        node = stack.pop()

        if node.right:
            stack.append(node.right)
        if node.left:
            stack.append(node.left)
        if not node.left and not node.right:
            yield node.val


class Solution:
    def leafSimilar(
        self, root1: TreeNode | None, root2: TreeNode | None
    ) -> bool:
        seq1 = leaf_value_seq(root1)
        seq2 = leaf_value_seq(root2)

        for a, b in zip_longest(seq1, seq2):
            if a != b:
                return False

        return True
