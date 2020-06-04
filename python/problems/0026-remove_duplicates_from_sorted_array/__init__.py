from typing import List


class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        current_num = None
        length = 0

        for _ in range(0, len(nums)):
            list_num = nums[length]

            if current_num != list_num:
                current_num = list_num
                length += 1
            else:
                del nums[length]

        return length
