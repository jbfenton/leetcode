class MinStack:
    def __init__(self):
        self._stack = list()

    def push(self, x: int) -> None:
        min_num = self._stack[-1][1] if self._stack else x
        self._stack.append((x, min_num if min_num < x else x))

    def pop(self) -> None:
        self._stack.pop()

    def top(self) -> int:
        return self._stack[-1][0]

    def getMin(self) -> int:
        return self._stack[-1][1]
