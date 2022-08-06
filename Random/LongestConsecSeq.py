from typing import *


class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        largest_curr = largest_so_far = nums[0]

        for i in range(1, len(nums)):
            largest_curr = max(nums[i] + largest_curr, nums[i])
            largest_so_far = max(largest_so_far, largest_curr)

        return largest_so_far

nums = [-2,1,-3,4,-1,2,1,-5,4]
nums = [-2, 1]
nums = [5,4,-1,7,8]
solution = Solution()
print(solution.maxSubArray(nums))