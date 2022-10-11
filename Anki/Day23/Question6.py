from typing import *

class Solution:
    def maximumScore(self, nums: List[int], multipliers: List[int]) -> int:
        self.nums, self.multipliers = nums, multipliers
        self.memo = {}
        self.m, self.n = len(self.multipliers), len(nums)
        left_pointer, right_pointer = 0, len(nums) - 1
        return self.dp(left_pointer, right_pointer)



    def dp(self, left_pointer, right_pointer):
        key = (left_pointer, right_pointer)
        curr_iteration = self.n - 1 + left_pointer - right_pointer
        if curr_iteration >= self.m:
            return 0
        elif key in self.memo:
            return self.memo[key]

        take_left = self.nums[left_pointer] * self.multipliers[curr_iteration] + self.dp(left_pointer + 1, right_pointer)
        take_right = self.nums[right_pointer] * self.multipliers[curr_iteration] + self.dp(left_pointer, right_pointer - 1)
        answer = max(take_right, take_left)
        self.memo[key] = answer

        return answer

nums = [-5,-3,-3,-2,7,1]
multipliers = [-10,-5,3,4,6]
# nums = [1,2,3]
# multipliers = [3,2,1]
solution = Solution()
print(solution.maximumScore(nums, multipliers))
