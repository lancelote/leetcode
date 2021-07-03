class OrderedStream:
    def __init__(self, n: int):
        self.data: list[str] = [""] * n
        self.ptr = 0

    def insert(self, id_key: int, value: str) -> list[str]:
        self.data[id_key - 1] = value
        chunk: list[str] = []

        while self.ptr < len(self.data) and (item := self.data[self.ptr]):
            chunk.append(item)
            self.ptr += 1

        return chunk
