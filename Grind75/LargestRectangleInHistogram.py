from typing import *


class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        max_height, max_width, max_area = heights[0], 1, heights[0]
        for i in range(1, len(heights)):
            curr_height = heights[i]
            if curr_height < max_height:
                if curr_height * (max_width + 1) > max_area:
                    max_height, max_width, max_area = curr_height, max_width + 1, curr_height * (max_width + 1)
            elif curr_height == max_height:
                max_width, max_area = max_width + 1, max_area + max_height
            else:
                if curr_height > max_area + max_height:
                    max_height, max_width, max_area = curr_height, 1, curr_height
                else:
                    max_width, max_area = max_width + 1, max_area + max_height

        return max_area


heights = [2,1,5,6,2,3]
solution = Solution()
print(solution.largestRectangleArea(heights))