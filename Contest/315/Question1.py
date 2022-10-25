from typing import *


class Solution:
    def findMaxK(self, nums: List[int]) -> int:
        num_dict = {k: 1 for k in nums}
        max_int = float('-inf')
        for num in nums:
            if -num in num_dict:
                max_int = max(max_int, num)

        return max_int if max_int != float('-inf') else -1

nums = [-1,2,-3,3]
nums = [-1,10,6,7,-7,1]
solution = Solution()
print(solution.findMaxK(nums))