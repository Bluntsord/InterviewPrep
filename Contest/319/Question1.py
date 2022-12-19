from typing import *


class Solution:
    def convertTemperature(self, celsius: float) -> List[float]:
        return [celsius + 273.15, celsius * 1.8 + 32]

solution = Solution()
print(solution.convertTemperature(36.5))