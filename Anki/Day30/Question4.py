from typing import *

class Solution:
    def countQuadruplets(self, nums: List[int]) -> int:
        prefix_arr = [[0, 0] for i in range(len(nums))]
        for i in range(1, len(nums)):
            for j in range(i):
                if nums[j] < nums[i]:
                    nums[i][0] += 1
                elif nums[j] > nums[i]:
                    nums[i][1] += 1
                
        print(prefix_arr)

solution = Solution()
nums = [1,3,2,4,5]
print(solution.countQuadruplets(nums))