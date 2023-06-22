from typing import *

class Solution:
    def minCost(self, nums: List[int], cost: List[int]) -> int:
        self.nums = nums
        self.cost = cost

        curr_min, curr_max = min(nums), max(nums)
        answer = float('inf')
        for i in range(curr_min, curr_max):
            answer = min(answer, self.curr_cost(i))

        return answer

    def curr_cost(self, target):
        answer = 0
        for i in range(len(self.nums)):
            curr = abs(target - self.nums[i]) * self.cost[i]
            answer += curr

        return answer

nums = [1,3,5,2]
cost = [2,3,1,14]
solution = Solution()
print(solution.minCost(nums, cost))