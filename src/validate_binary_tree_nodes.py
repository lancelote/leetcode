class Solution:
    def validateBinaryTreeNodes(
        self, n: int, left_child: list[int], right_child: list[int]
    ) -> bool:
        with_parents = set(left_child + right_child)
        with_parents.discard(-1)

        if len(with_parents) == n:
            return False  # no root

        root = -1
        for i in range(n):
            if i not in with_parents:
                root = i
                break

        visited: set[int] = set()

        def dfs(node: int) -> bool:
            if node == -1:
                return True
            if node in visited:
                return False
            visited.add(node)

            return dfs(left_child[node]) and dfs(right_child[node])

        return dfs(root) and len(visited) == n
