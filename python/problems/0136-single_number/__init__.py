from typing import List


class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        lookup = set()

        for num in nums:
            if num not in lookup:
                lookup.add(num)
            else:
                lookup.remove(num)

        return lookup.pop()
