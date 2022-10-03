from typing import *


class Solution:
    def longestSubarray(self, nums: List[int]) -> int:
        num_max = max(nums)
        answer = 0
        left_pointer, right_pointer = 0, 0
        while right_pointer < len(nums):
            right_num = nums[right_pointer]
            while right_num == num_max:
                right_pointer += 1
                if right_pointer >= len(nums):
                    break
                right_num = nums[right_pointer]
            answer = max(answer, right_pointer - left_pointer)
            left_pointer = right_pointer + 1
            right_pointer = left_pointer
        return answer



nums = [1,2,3,3,2,2]
nums = [1,2,3,4]
solution = Solution()
print(solution.longestSubarray(nums))