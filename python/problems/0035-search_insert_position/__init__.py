from typing import List


class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        num_len = len(nums)

        for i in range(num_len - 1):
            if nums[i] >= target:
                return i

        if nums[-1] >= target:
            return num_len - 1

        return num_len
