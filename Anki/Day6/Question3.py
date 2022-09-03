import bisect
import random
from typing import *


class Solution:

    def __init__(self, w: List[int]):
        self.sum = 0
        self.ranges = []
        acc = 0
        for i in range(w):
            acc += w[i]
            self.sum += w[i]
            self.ranges.append(acc)

    def pickIndex(self) -> int:
        rand = random.randint(0, self.sum)
        index = bisect.bisect_left(rand, self.ranges)
        return index


