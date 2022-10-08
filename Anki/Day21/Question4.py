from typing import *


class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        stack = set()
        for i in range(len(nums)):
            if nums[i] in stack:
                stack.remove(nums[i])
            else:
                stack.add(nums[i])

        return list(stack)[0]