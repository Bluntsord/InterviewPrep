from typing import *

# Quick select
class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        self.nums = nums
        self.k = len(nums) - k
        return self.helper(0, len(nums) - 1)

    def helper(self, start, end):
        mid = self.partition(start, end)
        if mid == self.k:
            return self.nums[mid]
        elif mid < self.k:
            return self.helper(mid + 1, end)
        else:
            return self.helper(start, mid - 1)



    def partition(self, start, end):
        pivot = self.nums[start]
        left_pointer = start
        for i in range(start, end + 1):
            if self.nums[i] <= pivot:
                self.nums[i], self.nums[left_pointer] = self.nums[left_pointer], self.nums[i]
                left_pointer += 1

        self.nums[left_pointer - 1], self.nums[start] = self.nums[start], self.nums[left_pointer - 1]
        return left_pointer - 1


nums = [3,2,1,5,6,4]
k = 2
solution = Solution()
print(solution.findKthLargest(nums, k))