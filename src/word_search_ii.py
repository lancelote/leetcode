SHIFTS = [
    (-1, 0),
    (0, +1),
    (+1, 0),
    (0, -1),
]


class Node:
    def __init__(self) -> None:
        self.end = False
        self.children: dict[str, Node] = {}

    def add_word(self, word: str) -> None:
        current = self

        for char in word:
            if char not in current.children:
                current.children[char] = Node()
            current = current.children[char]

        current.end = True

    def prune(self, word: str) -> None:
        current = self

        node_and_char: list[tuple[Node, str]] = []
        for char in word:
            node_and_char.append((current, char))
            current = current.children[char]

        for node, char in reversed(node_and_char):
            if len(node.children[char].children) == 0:
                del node.children[char]
            else:
                return


class Solution:
    def findWords(self, board: list[list[str]], words: list[str]) -> list[str]:
        assert board
        assert board[0]

        root = Node()

        for word in words:
            root.add_word(word)

        rows = len(board)
        cols = len(board[0])

        result: list[str] = []
        visited: set[tuple[int, int]] = set()

        def dfs(r: int, c: int, node: Node, word: str) -> None:
            if (
                not (0 <= r < rows and 0 <= c < cols)
                or (r, c) in visited
                or board[r][c] not in node.children
            ):
                return

            visited.add((r, c))
            node = node.children[board[r][c]]
            word += board[r][c]

            if node.end:
                result.append("".join(word))
                root.prune(word)
                node.end = False

            for dr, dc in SHIFTS:
                dfs(r + dr, c + dc, node, word)

            visited.remove((r, c))

        for r in range(rows):
            for c in range(cols):
                dfs(r, c, root, "")

        return result
