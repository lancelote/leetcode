class MountainArray:
    def __init__(self, arr: list[int]) -> None:
        self.arr = arr

    def get(self, index: int) -> int:
        return self.arr[index]

    def length(self) -> int:
        return len(self.arr)


class Solution:
    def findInMountainArray(
        self,
        target: int,
        mountain_arr: MountainArray,
    ) -> int:
        length = mountain_arr.length()

        def get_peak() -> int:
            left = 1
            right = length - 2

            while left <= right:
                middle = (left + right) // 2

                to_left = mountain_arr.get(middle - 1)
                mid_val = mountain_arr.get(middle)
                to_right = mountain_arr.get(middle + 1)

                if to_left < mid_val < to_right:
                    left = middle + 1
                elif to_left > mid_val > to_right:
                    right = middle - 1
                else:
                    return middle

            raise ValueError

        def search(left: int, right: int, dec: bool = False) -> int:
            while left <= right:
                middle = (right - left) // 2 + left
                mid_val = mountain_arr.get(middle)

                if mid_val == target:
                    return middle
                elif mid_val > target:
                    if dec:
                        left = middle + 1
                    else:
                        right = middle - 1
                elif mid_val < target:
                    if dec:
                        right = middle - 1
                    else:
                        left = middle + 1
                else:
                    return middle

            return -1

        peak = get_peak()
        peak_val = mountain_arr.get(peak)

        if target > peak_val:
            return -1
        elif target == peak_val:
            return peak

        left_result = search(0, peak - 1)

        if left_result != -1:
            return left_result

        right_result = search(peak + 1, length - 1, dec=True)

        if right_result != -1:
            return right_result

        return -1
