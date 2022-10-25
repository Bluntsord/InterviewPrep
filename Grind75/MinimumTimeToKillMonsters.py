import bisect
import math
from typing import *
import queue as q

class Solution:
    def minimumTime(self, power: List[int]) -> int:
        days, gain, curr_power = 0, 1, 0
        power.sort()



power = [1,2,4,9]
solution = Solution()
print(solution.minimumTime(power))



