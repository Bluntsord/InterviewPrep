import bisect
from typing import *


class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        self.answer = []
        insert_order = bisect.bisect_left(intervals, newInterval[0], key=lambda x: x[0])
        for i in range(len(intervals)):
            if i == insert_order:
                self.handle_stack(newInterval)
            self.handle_stack(intervals[i])
        return self.answer

    def handle_stack(self, interval):
        latest_interval = self.answer[-1]
        if latest_interval[1] >= interval[0]:
            self.answer.pop()
            temp = [latest_interval[0], interval[1]]
            self.answer.append(temp)
        else:
            self.answer.append(interval)


intervals = [[1,3],[6,9]]
newInterval = [2,5]
solution = Solution()
print(solution.insert(intervals, newInterval))


