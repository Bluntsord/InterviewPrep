from typing import *


class Solution:
    def countQuadruplets(self, nums: List[int]) -> int:
        prefix_arr = [[0, 0] for i in range(len(nums))]

