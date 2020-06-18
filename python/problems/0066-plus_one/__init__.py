from typing import List


class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        index = -1
        total = digits[index] + 1
        carry = total // 10
        digits[index] = total % 10

        while carry > 0:
            index -= 1

            if index < -len(digits):
                digits[0] = total % 10
                digits = [total // 10] + digits
                break
            else:
                total = digits[index] + carry
                carry = total // 10
                digits[index] = total % 10

        return digits
