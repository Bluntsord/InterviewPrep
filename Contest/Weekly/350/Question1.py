from typing import *

class Solution:
    def distanceTraveled(self, mainTank: int, additionalTank: int) -> int:
        if mainTank < 5:
            return mainTank * 10

        additional_tank_consumed = min((mainTank // 5), additionalTank)
        additional_tank_left = additionalTank - additional_tank_consumed
        next_tank = additional_tank_left + (mainTank % 5)

        curr_tank_used = mainTank + additional_tank_consumed
        return curr_tank_used * 10 + self.distanceTraveled(next_tank, additional_tank_left)

solution = Solution()
print(solution.distanceTraveled(9, 2))