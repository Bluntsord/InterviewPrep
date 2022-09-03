class MinStack:

    def __init__(self):
        self.stack = []

    def push(self, val: int) -> None:
        prev_min = val if len(self.stack) == 0 else min(self.stack[-1][0], val)
        curr = (prev_min, val)
        self.stack.append(curr)

    def pop(self) -> None:
        self.stack.pop()

    def top(self) -> int:
        return self.stack[len(self.stack) - 1][1]

    def getMin(self) -> int:
        return self.stack[-1][0]
