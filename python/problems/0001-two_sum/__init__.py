from typing import List


class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        diffs = {}

        for index, num in enumerate(nums):
            diff = target - num

            if diff in diffs:
                return [index, diffs[diff]]
            else:
                diffs[num] = index
