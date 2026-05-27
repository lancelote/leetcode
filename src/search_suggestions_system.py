class Node:
    def __init__(self) -> None:
        self.children: dict[str, Node] = {}
        self.is_final = False


class Trie:
    def __init__(self) -> None:
        self.root = Node()

    def insert_word(self, word: str) -> None:
        current = self.root

        for x in word:
            if x in current.children:
                current = current.children[x]
            else:
                new_node = Node()
                current.children[x] = new_node
                current = new_node

        current.is_final = True

    def insert_words(self, words: list[str]) -> None:
        for word in sorted(words):
            self.insert_word(word)

    def get_three_by_prefix(self, prefix: list[str]) -> list[str]:
        result: list[str] = []

        path: list[str] = []
        start_node = self.root

        for x in prefix:
            if x in start_node.children:
                start_node = start_node.children[x]
                path.append(x)
            else:
                return []

        def dfs(node: Node) -> None:
            if len(result) == 3:
                return

            if node.is_final:
                result.append("".join(path))

            for k, v in node.children.items():
                path.append(k)
                dfs(v)
                path.pop()

        dfs(start_node)
        return result


class Solution:
    def suggestedProducts(
        self, products: list[str], search_word: str
    ) -> list[list[str]]:
        result: list[list[str]] = []

        trie = Trie()
        trie.insert_words(products)

        prefix: list[str] = []
        for x in search_word:
            prefix.append(x)
            result.append(trie.get_three_by_prefix(prefix))

        return result
