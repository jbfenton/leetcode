from typing import List


class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        start = 0
        end = len(nums) - 1

        counter = 0

        while start < len(nums) and start <= end:
            if nums[end] == val:
                end -= 1
            else:
                if nums[start] == val:
                    nums[start], nums[end] = nums[end], nums[start]

                start += 1
                counter += 1

        return counter
