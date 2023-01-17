from typing import *


class Solution(object):
    def unequalTriplets(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        answer = 0
        for i in range(len(nums)):
            for j in range(len(nums)):
                for k in range(len(nums)):
                    if not (i < j < k):
                        continue

                    cond = nums[i] != nums[j] and nums[i] != nums[k] and nums[j] != nums[k]
                    answer += 1 if cond else 0

        return answer



nums = [4,4,2,4,3]
solution = Solution()
print(solution.unequalTriplets(nums))