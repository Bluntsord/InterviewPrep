from typing import *


class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        self.nums = nums
        self.set = set()
        self.answer = []

        for i in range(len(nums) + 1):
            self.backTracking(i, 0)

        return self.answer

    def backTracking(self, length, start):
        if len(self.set) == length:
            self.answer.append(list(self.set))
            return

        for i in range(start, len(self.nums)):
            num = self.nums[i]
            if num in self.set:
                continue
            self.set.add(num)

            self.backTracking(length, i + 1)

            self.set.remove(num)

solution = Solution()
nums = [1, 2, 3, 4]
print(solution.subsets(nums))