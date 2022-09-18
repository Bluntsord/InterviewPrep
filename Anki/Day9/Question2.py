from typing import *


class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        self.nums = nums
        self.k = len(nums) - k
        left_pointer, right_pointer = 0, len(nums) - 1
        while left_pointer <= right_pointer:
            mid = self.partition(left_pointer, right_pointer)
            if mid == self.k:
                return self.nums[mid]
            elif mid < self.k:
                left_pointer = mid + 1
            else:
                right_pointer = mid - 1

        return self.nums[mid]


    def partition(self, start, end):
        if start == end:
            return start
        pivot = self.nums[start]
        left_pointer = start

        for i in range(start, end + 1):
            if self.nums[i] <= pivot:
                self.nums[left_pointer], self.nums[i] = self.nums[i], self.nums[left_pointer]
                left_pointer += 1
        self.nums[left_pointer - 1], self.nums[start] = self.nums[start], self.nums[left_pointer - 1]

        return left_pointer - 1

solution = Solution()
nums = [3,2,1,5,6,4]
k = 2
print(solution.findKthLargest(nums, k))