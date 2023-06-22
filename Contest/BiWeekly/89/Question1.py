from typing import *


class Solution:
    def countTime(self, time: str) -> int:
        acc = 1
        time_arr = [time[0], time[1], time[3], time[4]]
        if time_arr[0] == "?" and time_arr[1] == "?":
            acc *= 24
        elif time[0] == "?" and int(time_arr[1]) > 4:
            acc *= 2
        elif time[0] == "?" and int(time_arr[1]) <= 4:
            acc *= 3
        elif time[1] == "?" and int(time_arr[0]) < 2:
            acc *= 10
        elif time[1] == "?" and int(time_arr[0]) == 2:
            acc *= 5

        if time_arr[2] == "?" and time_arr[3] == "?":
            if time_arr[0] == "2" and time_arr[1] == "?":
                acc *= 48
            elif time_arr[0] == "2" and time_arr[1] == "4":
                acc *= 1
            elif time_arr[0] == "2":
                acc *= 60
            elif time_arr[0] != 0:
                acc *= 60
        elif time_arr[3] == "?":
            acc *= 10
        elif time_arr[2] == "?":
            acc *= 7 if time_arr[3] == "0" else 6

        return acc


solution = Solution()
time = "2?:??"
# time = "0?:0?"
# time = "?5:00"
print(solution.countTime(time))
