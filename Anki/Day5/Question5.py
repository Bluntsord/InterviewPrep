import bisect
from typing import *


class Solution:
    def search(self, nums: List[int], target: int) -> int:
        self.nums = nums
        i = bisect.bisect_left(nums, self.helper(target), key=self.helper)
        return i if (i < len(nums) and nums[i] == target) else -1

    def helper(self, num):
        return num < self.nums[0], num

nums = [4,5,6,7,0,1,2]
# nums = [i for i in range(10)]
target = 0
solution = Solution()
print(solution.search(nums, target))
