from typing import *


class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        target = sum(i for i in range(len(nums)))
        actual = sum(nums)
        return actual - target

nums = [1,3,4,2,2]
solution = Solution()
print(solution.findDuplicate(nums))