from typing import *

class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals = intervals.sort(key= lambda x: x[0])
        stack = [intervals[0]]

        for interval in intervals[1:]:
            top_of_stack = stack[-1]

            if top_of_stack[1] >= interval[0]:
                stack.pop()
                stack.append([top_of_stack[0], max(interval[1], top_of_stack[1])])
            else:
                stack.append(interval)

        return stack


