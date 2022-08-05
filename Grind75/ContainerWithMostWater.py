from typing import *

class Solution:
    def maxArea(self, height: List[int]) -> int:
        max_so_far = 0
        left_ptr, right_ptr = 0, len(height) - 1

        while left_ptr < right_ptr:
            left_height, right_height = height[left_ptr], height[right_ptr]
            width = right_ptr - left_ptr
            curr_area = min(left_height, right_height) * width
            if left_height <= right_height:
                left_ptr += 1
            else:
                right_ptr -= 1
            max_so_far = max(max_so_far, curr_area)

        return max_so_far

height = [1,1]
solution = Solution()
print(solution.maxArea(height))
