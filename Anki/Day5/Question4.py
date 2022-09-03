from typing import *
import math

class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        target = math.floor(len(nums)/2)
        nums_dict = {}
        for num in nums:
            nums_dict[num] = nums_dict.get(num, 0) + 1
            if nums_dict[num] > target:
                return nums_dict[num]

        return -1