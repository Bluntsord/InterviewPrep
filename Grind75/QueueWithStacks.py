class MyQueue(object):

    def __init__(self):
        self.first_stack = []
        self.second_stack = []
        self.front = None

    def push(self, x):
        """
        :type x: int
        :rtype: None
        """
        if len(self.first_stack) == 0:
            self.front = x
        self.first_stack.append(x)


    def pop(self):
        """
        :rtype: int
        """
        if self.empty():
            return None

        elif len(self.second_stack) == 0:
            while len(self.first_stack) != 0:
                curr = self.first_stack.pop()
                self.second_stack.append(curr)
        return self.second_stack.pop()

    def peek(self):
        """
        :rtype: int
        """
        if len(self.second_stack) == 0:
            return self.front
        return self.second_stack.pop()

    def empty(self):
        """
        :rtype: bool
        """
        return len(self.second_stack) == 0 and len(self.first_stack) == 0
