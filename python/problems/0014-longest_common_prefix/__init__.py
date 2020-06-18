from typing import List


class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        if not strs:
            return ""

        shortest = min(strs, key=len)
        index = 0
        prefix = []

        while index < len(shortest):
            current = shortest[index]

            for word in strs:
                if word[index] != current:
                    return "".join(prefix)

            prefix.append(current)
            index += 1

        return "".join(prefix)
