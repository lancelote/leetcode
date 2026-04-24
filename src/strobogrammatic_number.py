class Solution:
    def isStrobogrammatic(self, num: str) -> bool:
        can_rotate = {"0", "1", "6", "8", "9"}
        mirrored = {"0", "1", "8"}

        left, right = 0, len(num) - 1

        while left <= right:
            if num[left] not in can_rotate:
                return False
            if num[right] not in can_rotate:
                return False

            if num[left] in mirrored or num[right] in mirrored:
                if num[left] != num[right]:
                    return False
            elif num[left] == num[right]:
                return False

            left += 1
            right -= 1

        return True
