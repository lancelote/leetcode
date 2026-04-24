class Solution:
    def nextGreaterElement(
        self,
        nums1: list[int],
        nums2: list[int],
    ) -> list[int]:
        stack: list[int] = []
        hashmap: dict[int, int] = {}

        for x in nums2:
            while stack and x > stack[-1]:
                hashmap[stack.pop()] = x
            stack.append(x)

        return [hashmap.get(x, -1) for x in nums1]
