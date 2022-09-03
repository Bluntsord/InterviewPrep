class MyQueue:
    def __init__(self):
        self.first_stack = []
        self.second_stack = []

    def push(self, x: int) -> None:
        self.first_stack.append(x)

    def pop(self) -> int:
        if len(self.second_stack) == 0:
            self.first_stack.extend(reversed(self.second_stack))
        return self.second_stack.pop()

    def peek(self) -> int:
        if len(self.second_stack) == 0:
            self.first_stack.extend(reversed(self.second_stack))
        return self.second_stack[-1]

    def empty(self) -> bool:
        self.first_stack = []
        self.second_stack = []
