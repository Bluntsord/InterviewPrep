from typing import *

class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        min_curr = max_curr = max_so_far = nums[0]
        for i in range(1, len(nums)):
            temp = max_curr
            max_curr = max(max_curr * nums[i], nums[i], min_curr * nums[i])
            min_curr = min(temp * nums[i], nums[i], min_curr * nums[i])
            max_so_far = max(max_curr, max_so_far)

        return max_so_far

nums = [-4,-3,-2]
solution = Solution()
print(solution.maxProduct(nums))