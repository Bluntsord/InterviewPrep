from typing import *


class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        self.nums, self.acc, self.answer = nums, [], []
        self.backTracking(0)
        return self.answer

    def backTracking(self, pointer):
        if pointer > len(self.nums):
            return
        elif pointer == len(self.nums):
            self.answer.append(self.acc[:])
            return

        for i in range(len(self.nums)):
            if self.nums[i] in self.acc:
                continue

            self.acc.append(self.nums[i])

            self.backTracking(pointer + 1)

            self.acc.pop()

nums = [1,2,3]
solution = Solution()
print(solution.permute(nums))
