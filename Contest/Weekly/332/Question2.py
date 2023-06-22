import bisect
from typing import *


class Solution:
    def countFairPairs(self, nums: List[int], lower: int, upper: int) -> int:
        nums.sort()

        answer = 0
        for i in range(len(nums)):
            curr = nums[i]
            left_bound = bisect.bisect_left(nums, lower - curr)
            right_bound = bisect.bisect_right(nums, upper - curr)

            if right_bound <= i:
                continue
            answer += right_bound - max(i + 1, left_bound)

        return answer


solution = Solution()
nums = [0,0,0,0,0,0]
lower = 0
upper = 0
print(solution.countFairPairs(nums, lower, upper))
