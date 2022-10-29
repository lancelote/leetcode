class Node:
    def __init__(self) -> None:
        self.children: dict[str, Node] = {}


class Trie:
    def __init__(self) -> None:
        self.root = Node()

    def add_word(self, word: str) -> None:
        node = self.root

        for char in word:
            if char not in node.children:
                node.children[char] = Node()
            node = node.children[char]


def search(node: Node, word: str, i: int = 0, replace: int = 2) -> bool:
    if replace == -1:
        return False
    if i == len(word):
        return True

    for char, node in node.children.items():
        if search(node, word, i + 1, replace - (char != word[i])):
            return True
    return False


class Solution:
    def twoEditWords(
        self, queries: list[str], dictionary: list[str]
    ) -> list[str]:
        result: list[str] = []
        trie = Trie()

        for word in dictionary:
            trie.add_word(word)

        for word in queries:
            if search(trie.root, word):
                result.append(word)

        return result
