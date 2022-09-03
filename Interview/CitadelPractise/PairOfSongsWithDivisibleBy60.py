from typing import *


class Solution:
    def numPairsDivisibleBy60(self, time: List[int]) -> int:
        time_dict = {}
        answer = 0
        for i in range(len(time)):
            curr_time = time[i] % 60
            if curr_time == 0 and curr_time in time_dict:
                answer += time_dict[curr_time]
            elif 60 - curr_time in time_dict:
                answer += time_dict[60 - curr_time]
            time_dict[curr_time] = time_dict.get(curr_time, 0) + 1

        return answer

