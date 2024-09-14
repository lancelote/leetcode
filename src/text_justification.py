class Solution:
    def fullJustify(self, words: list[str], max_width: int) -> list[str]:
        raw_lines: list[list[str]] = []

        # construct lines without justification
        word_idx = 0

        while word_idx < len(words):
            line_length = 0
            line: list[str] = []

            while (word_idx < len(words)) and (
                line_length + bool(line) + len(words[word_idx]) <= max_width
            ):
                line_length += bool(line) + len(words[word_idx])
                line.append(words[word_idx])
                word_idx += 1

            raw_lines.append(line)

        # justify lines
        lines: list[str] = []

        for i in range(len(raw_lines) - 1):
            if len(raw_lines[i]) == 1:
                word = raw_lines[i][0]
                lines.append(word + " " * (max_width - len(word)))
                continue

            n_spaces = max_width - sum(len(word) for word in raw_lines[i])
            n_min_spaces = n_spaces // (len(raw_lines[i]) - 1)
            n_extra_spaces = n_spaces - n_min_spaces * (len(raw_lines[i]) - 1)

            justified: list[str] = []

            for word in raw_lines[i]:
                if not justified:
                    justified.append(word)
                else:
                    justified.append(" " * n_min_spaces)
                    if n_extra_spaces:
                        justified.append(" ")
                        n_extra_spaces -= 1
                    justified.append(word)

            lines.append("".join(justified))

        last_line = " ".join(raw_lines[-1])
        extra_space = max_width - len(last_line)
        lines.append(last_line + " " * extra_space)

        return lines
