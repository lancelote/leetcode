class Solution:
    def encode(self, text: list[str]) -> str:
        length = str(len(text))
        lengths = [str(len(block)) for block in text]
        return f"{length} {' '.join(lengths)} {''.join(text)}"

    def decode(self, data: str) -> list[str]:
        counter = 0

        def read_next_int() -> int:
            nonlocal counter
            read_array: list[str] = []

            while data[counter] != " ":
                read_array.append(data[counter])
                counter += 1
            counter += 1

            number = int("".join(read_array))
            return number

        def read_next_block_of(length: int) -> str:
            nonlocal counter
            block_array: list[str] = []

            for _ in range(length):
                block_array.append(data[counter])
                counter += 1

            return "".join(block_array)

        total_blocks = read_next_int()
        block_lengths = [read_next_int() for _ in range(total_blocks)]
        blocks = [read_next_block_of(length) for length in block_lengths]

        return blocks
