class MinStack:

    def __init__(self):
        self._stack = []

    def push(self, val: int) -> None:
        if not self._stack or val < self._stack[-1][1]:
            min_val = val
        else:
            min_val = self._stack[-1][1]
        self._stack.append((val, min_val))

    def pop(self) -> None:
        self._stack.pop()

    def top(self) -> int:
        return self._stack[-1][0]

    def getMin(self) -> int:
        return self._stack[-1][1]