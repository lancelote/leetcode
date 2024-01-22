class Node:
    def __init__(self) -> None:
        self.children: dict[str, Node] = {}
        self.is_end = False


class Trie:
    def __init__(self) -> None:
        self.root = Node()

    def insert(self, word: str) -> None:
        node = self.root

        for x in word:
            if x not in node.children:
                node.children[x] = Node()
            node = node.children[x]

        node.is_end = True

    def search(self, word: str) -> bool:
        node = self.root

        for x in word:
            if x not in node.children:
                return False
            node = node.children[x]

        return node.is_end

    def startsWith(self, prefix: str) -> bool:
        node = self.root

        for x in prefix:
            if x not in node.children:
                return False
            node = node.children[x]

        return True
