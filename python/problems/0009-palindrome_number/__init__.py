class Solution:
    def isPalindrome(self, x: int) -> bool:
        str_int = str(x)
        start = 0
        end = len(str_int) - 1

        if x < 0:
            return False

        while start < end < len(str_int):
            if str_int[start] != str_int[end]:
                return False

            start += 1
            end -= 1

        return True
