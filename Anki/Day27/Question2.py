from typing import *

class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort(key=lambda x: x[0])
        stack = [intervals[0]]
        for curr_interval in intervals[1:]:
            top_of_stack = stack[-1]
            if top_of_stack[1] >= curr_interval[0]:
                stack[-1] = [top_of_stack[0], max(top_of_stack[1], curr_interval[1])]
            else:
                stack.append(curr_interval)

        return stack



intervals_one = [[1,3],[2,6],[8,10],[15,18]]
intervals_two = [[1,4],[4,5]]
solution = Solution()
print(solution.merge(intervals_one))
print(solution.merge(intervals_two))
