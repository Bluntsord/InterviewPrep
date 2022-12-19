from typing import *

class Solution(object):
    def findKthLargest(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        self.arr = nums
        target = len(nums) - k
        low, high = 0, len(nums) - 1

        while low <= high:
            curr = self.partition(low, high)
            if curr == target:
                return self.arr[target]
            elif curr < target:
                low = curr + 1
            else:
                high = curr - 1

        return -1




    def partition(self, start, end):
        left_pointer = start + 1
        pivot = self.arr[start]
        for i in range(start + 1, end + 1):
            if self.arr[i] < pivot:
                self.arr[i], self.arr[left_pointer] = self.arr[left_pointer], self.arr[i]
                left_pointer += 1

        self.arr[left_pointer - 1], self.arr[start] = self.arr[start], self.arr[left_pointer - 1]

        return left_pointer - 1



solution = Solution()
nums = [3,2,1,5,6,4]
k = 5
print(solution.findKthLargest(nums, k))


