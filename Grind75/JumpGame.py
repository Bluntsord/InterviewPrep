from typing import *


class Solution:
    def canJump(self, nums: List[int]) -> bool:
        left_ptr, right_ptr = 0, nums[0]
        while left_ptr <= right_ptr:
            curr = nums[left_ptr]
            right_ptr = max(left_ptr + curr, right_ptr)
            if right_ptr >= len(nums) - 1:
                return True
            left_ptr += 1
        return False





        if counter < len(nums) - 1:
            return False
        return True


nums1 = [2,3,1,1,4]
answer1 = True

nums2 = [3,2,1,0,4]
answer2 = False

nums3 = [0, 2, 3]
answer3 = False

solution = Solution()
print(solution.canJump(nums1) == answer1)
print(solution.canJump(nums2) == answer2)
print(solution.canJump(nums3) == answer3)
