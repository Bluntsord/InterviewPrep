from typing import *


class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        self.nums, self.memo = nums, {}
        max_curr, max_so_far = nums[0], nums[0]

        for i in range(1, len(nums)):
            max_curr = max(max_curr + nums[i], 0)
            max_so_far = max(max_curr, max_so_far)

        return max_so_far

nums = [-2,1,-3,4,-1,2,1,-5,4]
solution = Solution()
print(solution.maxSubArray(nums))

