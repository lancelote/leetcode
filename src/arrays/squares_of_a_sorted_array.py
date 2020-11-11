from typing import List


class Solution:
    @staticmethod
    def get_non_negative_index(array: List[int]) -> int:
        for i, item in enumerate(array):
            if item >= 0:
                return i
        return len(array)

    def sortedSquares(self, array: List[int]) -> List[int]:
        result = []
        non_negative_index = self.get_non_negative_index(array)
        negative_index = non_negative_index - 1

        while negative_index >= 0 and non_negative_index < len(array):
            negative_item = array[negative_index]
            non_negative_item = array[non_negative_index]

            if non_negative_item > abs(negative_item):
                result.append(negative_item ** 2)
                negative_index -= 1
            else:
                result.append(non_negative_item ** 2)
                non_negative_index += 1

        while negative_index >= 0:
            result.append(array[negative_index] ** 2)
            negative_index -= 1

        while non_negative_index < len(array):
            result.append(array[non_negative_index] ** 2)
            non_negative_index += 1

        return result
