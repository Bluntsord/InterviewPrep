from typing import *


class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        max_so_far, max_curr, min_curr = nums[0], nums[0], nums[0]

        for i in range(1, len(nums)):
            temp_min, temp_max = min_curr, max_curr
            max_curr = max(max_curr * nums[i], nums[i], min_curr * nums[i])
            min_curr = min(min_curr * nums[i], nums[i], temp_max * nums[i])
            max_so_far = max(max_so_far, max_curr)

        return max_so_far

nums = [-1, -2, -9, -6]
solution = Solution()
print(solution.maxProduct(nums))