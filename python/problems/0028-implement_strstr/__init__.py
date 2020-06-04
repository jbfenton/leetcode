class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        if not needle:
            return 0

        cursor = 0
        needle_cursor = 0

        while cursor != len(haystack):
            if needle_cursor == len(needle):
                return cursor

            combined_cursor = cursor + needle_cursor
            if combined_cursor >= len(haystack):
                return -1
            elif haystack[combined_cursor] == needle[needle_cursor]:
                needle_cursor += 1
            else:
                cursor += 1
                needle_cursor = 0

        if cursor == len(haystack):
            return -1
        else:
            return cursor
