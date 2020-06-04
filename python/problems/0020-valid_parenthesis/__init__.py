class Solution:
    def isValid(self, s: str) -> bool:
        lookup = {
            ')': '(',
            ']': '[',
            '}': '{'
        }

        bracket_stack = []

        for bracket in s:
            if bracket in lookup:
                if bracket_stack and bracket_stack[-1] == lookup[bracket]:
                    bracket_stack.pop()
                else:
                    return False
            else:
                bracket_stack.append(bracket)

        if bracket_stack:
            return False
        else:
            return True
