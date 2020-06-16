class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        slow = 0
        fast = 0
        max_length = 0
        characters = set()

        while fast < len(s) and slow < len(s):
            if s[fast] not in characters:
                characters.add(s[fast])
                fast += 1
                max_length = max(max_length, fast - slow)
            else:
                characters.remove(s[slow])
                slow += 1

        return max_length
