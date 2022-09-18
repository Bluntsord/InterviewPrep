from typing import *


class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        self.nums = nums
        self.target = sum(nums)/2
        self.memo = {}
        if self.target % 2 == 1:
            return False
        return self.dp(0, 0)

    def dp(self, sum, pointer):
        key = str(sum) + "|" + str(pointer)
        if sum == self.target:
            return True
        elif pointer >= len(self.nums):
            return False
        elif key in self.memo:
            return self.memo[key]

        curr = self.nums[pointer]
        answer = self.dp(sum + curr, pointer + 1) or self.dp(sum, pointer + 1)
        self.memo[key] = answer

        return answer

