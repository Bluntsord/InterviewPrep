from typing import *

class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        k = k % len(nums)
        end = nums[len(nums) - k:]
        start = nums[: len(nums) - k]
        end.extend(start)

        for i in range(len(nums)):
            nums[i] = end[i]
        return nums

nums = [1, 2]
k = 5
solution = Solution()
print(solution.rotate(nums, k))