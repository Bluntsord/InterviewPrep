from typing import *


class Solution(object):
    def findKthLargest(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        low, high = 0, len(nums)
        target = len(nums) - k

        while low <= high:
            curr = self.partition(nums, low, high)
            if curr == target:
                return nums[curr]
            elif curr < target:
                low = curr + 1
            else:
                high = curr

        return -1

    def partition(self, arr, start, end):
        pivot = arr[start]
        smaller_pointer = start

        for i in range(start, end):
            if arr[i] <= pivot:
                arr[i], arr[smaller_pointer] = arr[smaller_pointer], arr[i]
                smaller_pointer += 1

        if smaller_pointer > start:
            arr[start], arr[smaller_pointer - 1] = arr[smaller_pointer - 1], arr[start]

        return smaller_pointer - 1

solution = Solution()
nums = [3,2,1,5,6,4]
print(solution.findKthLargest(nums, 5))