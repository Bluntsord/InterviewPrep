from typing import *


class Solution:
    def averageValue(self, nums: List[int]) -> int:
        total, number = 0, 0
        for i in range(len(nums)):
            if nums[i] % 3 == 0:
                total += nums[i]
                number += 1

        return total//number

solution = Solution()
nums = [1,3,6,10,12,15]
print(solution.averageValue(nums))