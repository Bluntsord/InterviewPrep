from typing import *


class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        num_dict = {}
        for num in num_dict:
            num_dict[num] = num_dict.get(num, 0) + 1
        for key, value in num_dict.items():
            if value == 1:
                return key
        return -1