from collections.abc import Iterator

from src.utils.binary_tree import TreeNode


def items_left(root: TreeNode | None) -> Iterator[int | None]:
    yield root.val if root else None

    if root:
        yield from items_left(root.left)
        yield from items_left(root.right)


def items_right(root: TreeNode | None) -> Iterator[int | None]:
    yield root.val if root else None

    if root:
        yield from items_right(root.right)
        yield from items_right(root.left)


class Solution:
    def isSymmetric(self, root: TreeNode | None) -> bool:
        if not root:
            return True

        for x, y in zip(items_left(root.left), items_right(root.right)):
            if x != y:
                return False

        return True
