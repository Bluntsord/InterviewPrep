from typing import *


class Solution:
    def trap(self, height: List[int]) -> int:
        answer, stack = 0, []
        for i, curr_height in enumerate(height):
            while stack and stack[-1] <= height:
                prev_index = stack.pop()
                if not stack:
                    break
                water_level = min(height[stack[-1]], curr_height) - height[prev_index]
                length = i - stack[-1] - 1
                answer += water_level * length
            stack.append(i)
        return answer
