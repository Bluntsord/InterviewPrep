from typing import *


class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        heights.append(0)
        answer, mono_stack = 0, []
        for i, height in enumerate(heights):
            while mono_stack and heights[mono_stack[-1]] > height:
                curr_height = heights[mono_stack.pop()]
                length = i - mono_stack[-1] - 1 if mono_stack else i
                answer = max(answer, length * curr_height)
            mono_stack.append(i)
        return answer

heights = [2,1,5,6,2,3]
# heights = [2, 4]
solution = Solution()
print(solution.largestRectangleArea(heights))


