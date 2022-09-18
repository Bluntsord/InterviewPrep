import bisect
from typing import *

class Interval:
    def __init__(self, start: int = None, end: int = None):
        self.start = start
        self.end = end

class Solution:
    def employeeFreeTime(self, schedule: '[[Interval]]') -> '[Interval]':
        stack = [interval for intervals in schedule for interval in intervals]
        return self.merge(stack)

    def merge(self, intervals):
        intervals.sort(key=lambda x: x.start)
        print(intervals)
        stack = [intervals[0]]

        for interval in intervals[1:]:
            latest_interval = stack[len(stack) - 1]

            # first case that we merge intervals
            if latest_interval.end >= interval.start:
                stack.pop()
                temp = [latest_interval.start, max(latest_interval.end, interval.end)]
                stack.append(temp)
            else:
                stack.append(interval)

        return stack


