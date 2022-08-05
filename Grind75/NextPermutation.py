import math
from typing import *


class Solution:
    def nextPermutation(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        self.nums = nums
        dest = -1
        for i in range(len(nums) - 1, 0, -1):
            if nums[i] > nums[i - 1]:
                dest = i - 1
                curr = nums[i - 1]
                break
        if dest == -1:
            return self.nums.sort()

        src = self.search(dest, curr)
        nums[dest], nums[src] = nums[src], nums[dest]
        self.reverse(dest + 1, len(self.nums) - 1)
        return self.nums

    def search(self, start, target):
        for i in range(len(self.nums) -1 , start - 1, - 1):
            if self.nums[i] > target:
                return i
        return len(self.nums) - 1

    def reverse(self, start, end):
        low = start
        high = end
        while low < high:
            self.nums[low], self.nums[high] = self.nums[high], self.nums[low]
            low += 1
            high -= 1

nums = [1,5,1,2]
solution = Solution()
print(nums[::-1])