class Solution:
    def maximumSegmentSum(
        self, nums: list[int], remove_indices: list[int]
    ) -> list[int]:
        # note: all items will be removed in the end
        biggest = 0
        result = []
        segments = {}

        # last remove operation leaves no items, hence max will be zero,
        # and we can skip this query from the calculation
        for remove_idx in reversed(remove_indices[1:]):
            segments[remove_idx] = (nums[remove_idx], 1)
            right_value, right_len = segments.get(remove_idx + 1, (0, 0))
            left_value, left_len = segments.get(remove_idx - 1, (0, 0))

            total = nums[remove_idx] + right_value + left_value
            segment_length = left_len + right_len + 1

            # update new segment boundaries
            segments[remove_idx + right_len] = (total, segment_length)
            segments[remove_idx - left_len] = (total, segment_length)

            biggest = max(biggest, total)
            result.append(biggest)

        # remember to add the last remove operation with sum of 0
        return result[::-1] + [0]
