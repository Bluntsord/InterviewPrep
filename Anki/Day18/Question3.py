from typing import *


class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        incr_stack = [(heights[0], 0)]
        answer = heights[0]
        for i in range(1, len(heights)):
            while incr_stack and incr_stack[-1][0] > heights[i]:
                prev_height, prev_index = incr_stack.pop()
                length = i - incr_stack[-1][1] - 1 if incr_stack else i
                answer = max(prev_height * length, answer)
            incr_stack.append((heights[i], i))

        return answer

heights = [2,1,5,6,2,3,2,2,2,2,2,2]
solution = Solution()
print(solution.largestRectangleArea(heights))