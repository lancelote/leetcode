LOWERCASE_A_UNICODE_CODE_POINT = 97


def coord_to_tuple(coordinates: str) -> tuple[int, int]:
    column = coordinates[0]
    row = coordinates[1]

    x = int(ord(column) - LOWERCASE_A_UNICODE_CODE_POINT)
    x += 1  # 1-based index
    y = int(row)

    return x, y


class Solution:
    def squareIsWhite(self, coordinates: str) -> bool:
        x, y = coord_to_tuple(coordinates)
        return (x + y) % 2 != 0
