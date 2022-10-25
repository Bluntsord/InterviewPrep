from typing import *


class Solution:
    def minCost(self, nums: List[int], cost: List[int]) -> int:
        num2 = [cost[i] * nums[i] for i in range(len(cost))]
        num_sum = sum(num2)
        var_sum = sum(cost)
        target = num_sum // var_sum
        answer = 0

        for i in range(len(cost)):
            curr = cost[i] * (target - nums[i])
            curr = -curr if curr < 0 else curr
            answer += curr

        return answer

solution = Solution()
nums = [735103,366367,132236,133334,808160,113001,49051,735598,686615,665317,999793,426087,587000,649989,509946,743518]
cost = [724182,447415,723725,902336,600863,287644,13836,665183,448859,917248,397790,898215,790754,320604,468575,825614]

print(solution.minCost(nums, cost))
