from typing import *


class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        tortoise = nums[0]
        hare = nums[nums[0]]

        while tortoise != hare:
            tortoise = nums[tortoise]
            hare = nums[nums[hare]]

        start = 0
        while start != tortoise:
            start = nums[start]
            tortoise = nums[tortoise]

        return start


nums = [1,3,4,2,2]
solution = Solution()
print(solution.findDuplicate(nums))