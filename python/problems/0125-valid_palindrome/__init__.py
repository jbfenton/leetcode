class Solution:
    def isPalindrome(self, s: str) -> bool:
        new_str = [char for char in s.lower() if char.isalnum()]

        start = 0
        end = len(new_str) - 1

        while start < len(new_str) and start < end:
            val_1 = new_str[start]
            val_2 = new_str[end]

            if val_1 != val_2:
                return False
            else:
                start += 1
                end -= 1

        return True
