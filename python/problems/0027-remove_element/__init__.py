from typing import List


class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        del_list = []

        for index, item in enumerate(nums):
            if item == val:
                del_list.append(index)

        counter = 0

        for item in del_list:
            del nums[item - counter]
            counter += 1

        return len(nums)
