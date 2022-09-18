from typing import *


class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        self.answer = []
        self.nums = nums
        self.backTracking(set())
        return self.answer

    def backTracking(self, curr: set):
        if len(curr) == len(self.nums):
            temp = list(curr)
            self.answer.append(temp)
            return

        for i in range(len(self.nums)):
            if self.nums[i] in curr:
                continue
            curr.add(self.nums[i])
            self.backTracking(curr)
            curr.remove(self.nums[i])



