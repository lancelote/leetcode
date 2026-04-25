SHIFTS = (
    (0, -1),  # up
    (1, 0),  # right
    (0, 1),  # down
    (-1, 0),  # left
)


class Solution:
    def floodFill(
        self, image: list[list[int]], sr: int, sc: int, color: int
    ) -> list[list[int]]:
        n_rows = len(image)
        n_cols = len(image[0])

        old_color = image[sr][sc]
        if old_color == color:
            return image

        to_fill = [(sr, sc)]

        while to_fill:
            r, c = to_fill.pop()
            image[r][c] = color

            for dr, dc in SHIFTS:
                nr = r + dr
                nc = c + dc

                if 0 <= nr < n_rows and 0 <= nc < n_cols:
                    if image[nr][nc] == old_color:
                        to_fill.append((nr, nc))

        return image
