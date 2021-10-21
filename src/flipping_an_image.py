Image = list[list[int]]


class Solution:
    @staticmethod
    def flip(image: Image) -> Image:
        return [row[::-1] for row in image]

    @staticmethod
    def invert(image: Image) -> Image:
        return [[int(not item) for item in row] for row in image]

    def flipAndInvertImage(self, image: Image) -> Image:
        return self.invert(self.flip(image))
