from typing import *


class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        self.answer = []
        self.nums = nums
        self.acc = set()
        self.backTracking(0, len(nums))
        self.visited = {}

        return self.answer


nums = [1,2,3]
solution = Solution()
print(solution.subsets(nums))
