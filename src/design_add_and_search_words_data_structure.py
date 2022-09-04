class Node:
    def __init__(self):
        self.children: dict[str, Node] = {}
        self.end = False


class WordDictionary:
    def __init__(self):
        self.root = Node()

    def addWord(self, word: str) -> None:
        node = self.root

        for char in word:
            if char not in node.children:
                node.children[char] = Node()
            node = node.children[char]

        node.end = True

    def search(self, word: str) -> bool:
        def dfs(node: Node, start: int = 0) -> bool:
            if start == len(word):
                return node.end

            for i in range(start, len(word)):
                if word[i] == ".":
                    return any(
                        dfs(child, i + 1) for child in node.children.values()
                    )
                elif word[i] in node.children:
                    return dfs(node.children[word[i]], i + 1)
                else:
                    return False

            raise ValueError

        return dfs(self.root)
