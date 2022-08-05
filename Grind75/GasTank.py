from typing import *


class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        if sum(gas) < sum(cost):
            return -1 

        diff = []
        for i in range(len(gas)):
            curr_diff = gas[i] - cost[i]
            diff.append(curr_diff)

        acc = 0
        start = 0
        for i in range(len(diff)):
            acc += diff[i]
            if acc < 0:
                acc = 0
                start = (i + 1) % len(diff)

        return start



gas = [1,2,3,4,5]
cost = [3,4,5,1,2]
solution = Solution()
print(solution.canCompleteCircuit(gas, cost))
