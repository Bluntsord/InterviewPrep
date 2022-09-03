from typing import *

class Solution:
    def trap(self, height: List[int]) -> int:
        left_acc = right_acc = 0
        left_max_heights = []
        right_max_heights = []
        for i in range(len(height)):
            left_acc = max(left_acc, height[i])
            left_max_heights.append(left_acc)

        for i in reversed(range(len(height))):
            right_acc = max(right_acc, height[i])
            right_max_heights.insert(0, right_acc)

        answer = 0
        for i in range(len(height)):
            curr = height[i]
            max_left = 0 if i == 0 else left_max_heights[i - 1]
            max_right = 0 if i == len(height) - 1 else right_max_heights[i + 1]
            top_up = min(max_right, max_left) - curr
            if top_up > 0:
                print(i, top_up)
                answer += top_up

        return answer



height = [0,1,0,2,1,0,1,3,2,1,2,1]
solution = Solution()
print(solution.trap(height))

