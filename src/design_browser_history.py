class Node:
    def __init__(self, page: str) -> None:
        self.page = page
        self.prev: Node | None = None
        self.next: Node | None = None

    def __repr__(self) -> str:
        return f'Node("{self.page}")'


class BrowserHistory:
    def __init__(self, homepage: str) -> None:
        self.node = Node(homepage)

    def visit(self, url: str) -> None:
        new_node = Node(url)
        self.node.next = new_node
        new_node.prev = self.node
        self.node = new_node

    def back(self, steps: int) -> str:
        while self.node.prev and steps:
            self.node = self.node.prev
            steps -= 1
        return self.node.page

    def forward(self, steps: int) -> str:
        while self.node.next and steps:
            self.node = self.node.next
            steps -= 1
        return self.node.page
