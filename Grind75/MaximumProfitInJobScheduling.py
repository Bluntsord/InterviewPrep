import bisect
from typing import *


class Solution:
    def jobScheduling(self, startTime: List[int], endTime: List[int], profit: List[int]) -> int:
        self.max_time = max(endTime)
        self.sorted_start_times = sorted(list(set(startTime)))
        self.starttime_dict = {}
        for i in range(len(startTime)):
            self.starttime_dict[startTime[i]] = self.starttime_dict.get(startTime[i], []) + [(endTime[i], profit[i])]
        self.memo = {}

        print(self.starttime_dict)
        return self.dp(min(startTime))

    def dp(self, curr_time):
        if curr_time >= self.max_time:
            return 0
        elif curr_time in self.memo:
            return self.memo[curr_time]

        take_curr_time = float('-inf')
        if curr_time in self.starttime_dict:
            for possible_end_time, possible_profit in self.starttime_dict[curr_time]:
                curr_profit = possible_profit + self.dp(possible_end_time)
                take_curr_time = max(take_curr_time, curr_profit)

        next_time = self.get_next_time(curr_time)
        drop_curr_time = self.dp(next_time)
        answer = max(take_curr_time, drop_curr_time)
        self.memo[curr_time] = answer

        return answer

    def get_next_time(self, curr_time):
        temp = bisect.bisect_right(self.sorted_start_times, curr_time)
        if temp == len(self.sorted_start_times):
            return float('inf')
        return self.sorted_start_times[bisect.bisect_right(self.sorted_start_times, curr_time)]

startTime = [1,2,3,3]
endTime = [3,4,5,6]
profit = [50,10,40,70]
solution = Solution()
print(solution.jobScheduling(startTime, endTime, profit))