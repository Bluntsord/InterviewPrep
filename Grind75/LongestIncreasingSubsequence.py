from typing import *


class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        self.nums = nums
        self.memo = []




nums = [10,9,2,5,3,7,101,18]
nums2 = [0, 1, 0, 3, 2, 3,4,5,67]

solution = Solution()
print(solution.lengthOfLIS(nums))
