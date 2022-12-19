from typing import *

class Solution:
    def findPoisonedDuration(self, timeSeries: List[int], duration: int) -> int:
        answer = 0
        for i in range(1, len(timeSeries)):
            answer += min(duration, timeSeries[i] - timeSeries[i - 1])

        return answer + duration

solution = Solution()
time_series = [1, 4]
duration = 2

print(solution.findPoisonedDuration(time_series, duration))

