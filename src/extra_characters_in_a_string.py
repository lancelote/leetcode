class Node:
    def __init__(self) -> None:
        self.end = False
        self.children: dict[str, Node] = {}

    def add_word(self, word: str) -> None:
        node = self

        for char in word:
            if char not in node.children:
                new_node = Node()
                node.children[char] = new_node
            node = node.children[char]

        node.end = True


class Solution:
    def minExtraChar(self, s: str, dictionary: list[str]) -> int:
        n = len(s)
        root = Node()

        for word in dictionary:
            root.add_word(word)

        dp = [0] * (n + 1)

        for start in range(n - 1, -1, -1):
            dp[start] = dp[start + 1] + 1

            node = root
            for end in range(start, n):
                char = s[end]
                if char not in node.children:
                    break
                node = node.children[char]
                if node.end:
                    dp[start] = min(dp[start], dp[end + 1])

        return dp[0]
