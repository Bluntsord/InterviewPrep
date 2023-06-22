from typing import *


class Solution:
    def haveConflict(self, event1: List[str], event2: List[str]) -> bool:
        event1 = list(map(self.change_str_to_time, event1))
        event2 = list(map(self.change_str_to_time, event2))
        if event1[0] > event2[0]:
            event1, event2 = event2, event1
        print(event1)
        print(event2)
        return event2[0] <= event1[1]


    def change_str_to_time(self, string):
        time = string[:2] + string[3:]
        return int(time)

event1 = ["10:00","11:00"]
event2 = ["14:00","15:00"]
solution = Solution()
print(solution.haveConflict(event1, event2))