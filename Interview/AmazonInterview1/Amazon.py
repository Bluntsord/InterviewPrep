from typing import *


class MovingAverage:

    def __init__(self, size: int):
        self.size = size
        self.array = []
        self.sum = 0

    def next(self, val: int) -> float:
        if self.size == len(self.array):
            self.sum -= self.array[0]
            self.sum += val
            self.array = self.array[1:]
            self.array.append(val)
            return self.sum/len(self.array)
        self.array.append(val)
        self.sum += val
        return self.sum/len(self.array)


# Your MovingAverage object will be instantiated and called as such:
# obj = MovingAverage(size)
# param_1 = obj.next(val)