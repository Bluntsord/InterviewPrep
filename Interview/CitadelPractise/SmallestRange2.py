from typing import *


class Solution:
    def smallestRangeII(self, nums: List[int], k: int) -> int:
        self.nums = nums
        self.k = k
        self.min = 0
        self.max = 0
        self.memo = {}
        pass

    def dp(self, pointer):
        if pointer >= self.nums:
            return 0
        elif pointer in self.memo:
            return self.memo[pointer]



