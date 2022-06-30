class Solution:
    def encode(self, text: list[str]) -> str:
        length = str(len(text))
        lengths = [str(len(block)) for block in text]
        return f"{length} {' '.join(lengths)} {''.join(text)}"

    def decode(self, data: str) -> list[str]:
        i = 0

        total_words_array = []
        while data[i] != " ":
            total_words_array.append(data[i])
            i += 1
        total_blocks = int("".join(total_words_array))
        i += 1

        block_lengths: list[int] = []

        for _ in range(total_blocks):
            block_length_array = []
            while data[i] != " ":
                block_length_array.append(data[i])
                i += 1
            block_length = int("".join(block_length_array))
            block_lengths.append(block_length)
            i += 1

        blocks: list[str] = []
        for block_length in block_lengths:
            block_array = []
            for _ in range(block_length):
                block_array.append(data[i])
                i += 1
            block = "".join(block_array)
            blocks.append(block)

        return blocks
