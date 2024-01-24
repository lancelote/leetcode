class Node:
    def __init__(self) -> None:
        self.children: dict[str, Node] = {}
        self.is_word = False


class Trie:
    def __init__(self) -> None:
        self.root = Node()

    def insert(self, word: str) -> None:
        node = self.root

        for x in word:
            if x not in node.children:
                node.children[x] = Node()
            node = node.children[x]

        node.is_word = True

    def find_node_by_prefix(self, prefix: str) -> Node | None:
        node = self.root

        for x in prefix:
            if x not in node.children:
                return None
            node = node.children[x]

        return node

    def find_all_with_prefix(self, prefix: str) -> list[str]:
        node = self.find_node_by_prefix(prefix)

        if not node:
            return []

        result: list[str] = []
        if node.is_word:
            result.append(prefix)

        postfix: list[str] = []

        def dfs(curr_node: Node) -> None:
            for x, next_node in curr_node.children.items():
                if len(result) == 3:
                    return

                postfix.append(x)

                if next_node.is_word:
                    result.append(prefix + "".join(postfix))

                dfs(next_node)
                postfix.pop()

        dfs(node)
        return result


class Solution:
    def suggestedProducts(
        self, products: list[str], search_word: str
    ) -> list[list[str]]:
        trie = Trie()

        for product in sorted(products):
            trie.insert(product)

        result: list[list[str]] = []
        prefix: list[str] = []

        for x in search_word:
            prefix.append(x)
            result.append(trie.find_all_with_prefix("".join(prefix)))

        return result
