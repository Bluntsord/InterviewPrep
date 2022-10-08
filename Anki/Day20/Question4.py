from typing import *


class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        hare, tortoise = nums[nums[0]], nums[0]
        while tortoise != hare:
            hare = nums[nums[hare]]
            tortoise = nums[tortoise]

        tortoise = nums[0]
        while tortoise != hare:
            tortoise = nums[hare]
            hare = nums[hare]

        return hare