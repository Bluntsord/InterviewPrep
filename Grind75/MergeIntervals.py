from typing import List


class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        stack = [intervals[0]]
        intervals.sort(key=lambda x: x[0])

        for interval in intervals[1:]:
            latest_interval = stack[len(stack) - 1]

            # first case that we merge intervals
            if latest_interval[1] >= interval[0]:
                stack.pop()
                temp = [latest_interval[0], interval[1]]
                stack.append(temp)
            else:
                stack.append(interval)

        return stack

intervals = [[1, 3], [2, 6], [8, 10], [15, 18]]
solution = Solution()
print(solution.merge(intervals))