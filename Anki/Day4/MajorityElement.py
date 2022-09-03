from typing import *
import math

class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        num_dict = {}
        for num in nums:
            num_dict[num] = num_dict.get(num, 0) + 1
            if num_dict[num] > math.floor(len(nums)/2):
                return num
        return -1