from typing import *


class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        self.nums = nums
        k = len(nums) - k
        left_pointer, right_pointer = 0, len(nums) - 1
        while True:
            counter = self.partition(left_pointer, right_pointer)
            if counter == k:
                break
            elif counter < k:
                left_pointer = counter + 1
            else:
                right_pointer = counter - 1

        return self.nums[counter]

    def partition(self, left_pointer, right_pointer):
        pivot = self.nums[right_pointer]
        counter = left_pointer
        for i in range(left_pointer, len(self.nums)):
            curr = self.nums[i]
            if curr < pivot:
                self.nums[i], self.nums[counter] = self.nums[counter], self.nums[i]
                counter += 1
        self.nums[right_pointer], self.nums[counter] = self.nums[counter], self.nums[right_pointer]
        return counter


nums = [3, 2, 1, 5, 6, 4]
k = 1
solution = Solution()
solution.nums = nums
print(solution.findKthLargest(nums, k))