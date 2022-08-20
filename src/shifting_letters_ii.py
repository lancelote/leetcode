class Solution:
    def shiftingLetters(self, s: str, shifts: list[list[int]]) -> str:
        move_changes = [0] * (len(s) + 1)

        for shift in shifts:
            start, end, direction = shift
            if direction == 1:
                move_changes[start] += 1
                move_changes[end + 1] -= 1
            else:
                move_changes[start] -= 1
                move_changes[end + 1] += 1

        move = 0
        result = []

        for i in range(len(s)):
            move += move_changes[i]
            if move:
                current_ord = ord(s[i]) - 97
                new_ord = (current_ord + move) % 26
                result.append(chr(new_ord + 97))
            else:
                result.append(s[i])

        return "".join(result)
