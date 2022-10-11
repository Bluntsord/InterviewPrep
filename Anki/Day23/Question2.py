from typing import *

class Solution:
    def rob(self, nums: List[int]) -> int:
        take, drop = nums[0], 0
        for num in nums[1:]:
            take, drop = num + drop, max(take, drop)
        return max(take, drop)