import bisect
from typing import *
from functools import lru_cache

class Solution:
    def jobScheduling(self, startTime: List[int], endTime: List[int], profit: List[int]) -> int:
        events = [[startTime[i], endTime[i], profit[i]] for i in range(len(startTime))]
        events.sort(key= lambda x: (x[0], x[1], -x[2]))

        @lru_cache(None)
        def dp(pointer):
            if pointer >= len(startTime):
                return 0

            curr_event = events[pointer]
            earliest_next_start_time = bisect.bisect_left(events, curr_event[1], key=lambda x: x[0])
            take_curr = curr_event[2] + dp(earliest_next_start_time)
            drop_curr = dp(pointer + 1)
            answer = max(take_curr, drop_curr)

            return answer

        return dp(0)



solution = Solution()
startTime = [1,2,3,3]
endTime = [3,4,5,6]
profit = [50,10,40,70]
print(solution.jobScheduling(startTime, endTime, profit))