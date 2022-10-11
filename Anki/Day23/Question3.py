from typing import *


class Solution(object):
    def minCostClimbingStairs(self, cost):
        """
        :type cost: List[int]
        :rtype: int
        """
        two_behind, one_behind = 0, 0
        for i in range(2, len(cost) + 1):
            two_behind, one_behind = one_behind, min(cost[i - 1] + one_behind, cost[i - 2] + two_behind)

        return one_behind


cost = [1,100,1,1,1,100,1,1,100,1]
# cost = [10, 15, 20]
solution = Solution()
print(solution.minCostClimbingStairs(cost))

