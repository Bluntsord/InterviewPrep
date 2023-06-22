from typing import *

class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        original_zero_count = 0
        for i in range(len(nums)):
            original_zero_count += 1 if nums[i] == 0 else 0
            nums[i] = 0 if nums[i] < 0 else nums[i]

        for i in range(len(nums)):
            if 0 < abs(nums[i]) < len(nums) and nums[abs(nums[i])] > 0:
                nums[abs(nums[i])] = -nums[abs(nums[i])]

        for i in range(1, len(nums)):
            if nums[i] > 0:
                return i

        return len(nums) - original_zero_count + 1


nums = [3,4,-1,1]
solution = Solution()
print(solution.firstMissingPositive(nums))